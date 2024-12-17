from playwright.sync_api import sync_playwright
import json
import time
import csv
import os
from datetime import datetime, timedelta
import re  # For extracting numbers from "hours ago"

# Read configuration from the JSON file
with open('config.json') as f:
    config = json.load(f)
    username = config['username']
    password = config['password']
    start_page = config['startPage']
    end_page = config['endPage']

# Function to fix missing year in dates
def fix_missing_year(date_str):
    """
    Add the current year to the date string if it doesn't already include a year.
    Handles "hours ago" cases by calculating relative dates.
    """
    current_time = datetime.now()  # Get the current date and time

    # Handle "X hours ago" format
    if "hours ago" in date_str:
        # Extract the number of hours
        hours_ago = int(re.search(r'(\d+)', date_str).group(1))
        calculated_time = current_time - timedelta(hours=hours_ago)
        return calculated_time.strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Attempt to parse the date with a year first
        return datetime.strptime(date_str, '%d %b %Y, %I:%M%p').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        # If the year is missing, append the current year and parse again
        date_with_year = f"{date_str} {current_time.year}"
        return datetime.strptime(date_with_year, '%d %b %I:%M%p %Y').strftime('%Y-%m-%d %H:%M:%S')

# Function to write song data to CSV
def write_to_csv(songs, csv_file):
    # Write data to CSV file after each page is scraped
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for song in songs:
            writer.writerow([song['song'], song['artist'], song['liked'], song['date']])

# Function to scrape data from Last.fm
def scrape_lastfm(username, password, start_page, end_page):
    # Define the CSV file where the data will be written
    csv_file = 'songs_data.csv'

    # Check if CSV file exists, if not, write the header
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['song', 'artist', 'liked', 'date'])

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser in headless mode
        page = browser.new_page()

        # Login to Last.fm
        page.goto('https://www.last.fm/login')
        page.fill('#id_username_or_email', username)
        page.fill('#id_password', password)
        page.click('.btn-primary')
        
        # Wait for the page to load completely
        page.wait_for_load_state("domcontentloaded")

        # Start scraping pages
        page_number = start_page
        while True:
            # If end_page is set and page_number exceeds it, stop the scrape
            if end_page != 0 and page_number > end_page:
                print(f"Reached the end page {end_page}. Stopping the scrape.")
                break  # Stop scraping if we've reached the end_page

            url = f'https://www.last.fm/user/{username}/library?page={page_number}'
            page.goto(url)
            page.wait_for_load_state("domcontentloaded")

            # Collect song data
            songs = page.query_selector_all('.tracklist-section tbody tr')
            if len(songs) == 0:
                print(f"Reached the last page or no songs found. Stopping the scrape.")
                break  # Stop scraping if no songs are found

            song_data = []
            for song in songs:
                # Check if the song is liked by looking at the `data-toggle-button-current-state` attribute in the div
                liked_status = song.query_selector('div[data-toggle-button-current-state]')
                
                # Check if the div exists and the 'data-toggle-button-current-state' is 'loved'
                if liked_status and liked_status.get_attribute('data-toggle-button-current-state') == 'loved':
                    liked = 'true'
                else:
                    liked = 'false'

                date_text = song.query_selector('.chartlist-timestamp span').inner_text().strip()

                # Fix the missing year or handle "hours ago" cases
                fixed_date = fix_missing_year(date_text)  # Fix the missing year here

                song_data.append({
                    'song': song.query_selector('.chartlist-name').inner_text().strip(),
                    'artist': song.query_selector('.chartlist-artist').inner_text().strip(),
                    'liked': liked,
                    'date': fixed_date,  # Use the fixed date
                })

            # Write to CSV immediately after scraping each page
            write_to_csv(song_data, csv_file)

            print(f"Scraped page {page_number}")

            page_number += 1  # Go to the next page

        browser.close()

# Call the scraping function
scrape_lastfm(username, password, start_page, end_page)
