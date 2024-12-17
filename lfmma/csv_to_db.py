import sqlite3
import os
import csv
from datetime import datetime
import json

# Function to create the database and tables
def create_db():
    conn = sqlite3.connect('songs_data.db')
    cursor = conn.cursor()

    # Artists table
    cursor.execute('''CREATE TABLE IF NOT EXISTS artists (
                        id INTEGER PRIMARY KEY,
                        artist_name TEXT UNIQUE)''')

    # Songs table
    cursor.execute('''CREATE TABLE IF NOT EXISTS songs (
                        id INTEGER PRIMARY KEY,
                        song_name TEXT,
                        artist_id INTEGER,
                        FOREIGN KEY(artist_id) REFERENCES artists(id))''')

    # Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE)''')

    # History table
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        song_id INTEGER,
                        liked BOOLEAN,
                        date TEXT,
                        day_name TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id),
                        FOREIGN KEY(song_id) REFERENCES songs(id))''')

    conn.commit()
    conn.close()

# Function to insert or update data
def insert_or_update_data(username, song_name, artist_name, liked, date):
    conn = sqlite3.connect('songs_data.db')
    cursor = conn.cursor()

    # Insert user if not exists
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = cursor.fetchone()
    if user_id is None:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        user_id = cursor.lastrowid
    else:
        user_id = user_id[0]

    # Insert artist if not exists
    cursor.execute("SELECT id FROM artists WHERE artist_name = ?", (artist_name,))
    artist_id = cursor.fetchone()
    if artist_id is None:
        cursor.execute("INSERT INTO artists (artist_name) VALUES (?)", (artist_name,))
        artist_id = cursor.lastrowid
    else:
        artist_id = artist_id[0]

    # Insert song if not exists
    cursor.execute("SELECT id FROM songs WHERE song_name = ? AND artist_id = ?", (song_name, artist_id))
    song_id = cursor.fetchone()
    if song_id is None:
        cursor.execute("INSERT INTO songs (song_name, artist_id) VALUES (?, ?)", (song_name, artist_id))
        song_id = cursor.lastrowid
    else:
        song_id = song_id[0]

    # Clean and validate date
    try:
        # For the format '2024-11-13 10:51:00'
        date = date.strip()  # Remove any leading or trailing spaces
        datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')  # Parse the date in the correct format
        day_name = datetime_object.strftime('%A')  # Get day name
    except ValueError:
        print(f"Skipping invalid date format: {date}")
        return  # Skip the invalid date and continue with the next row

    # Insert or update history
    cursor.execute("SELECT id FROM history WHERE user_id = ? AND song_id = ? AND date = ?", (user_id, song_id, date))
    history_entry = cursor.fetchone()
    if history_entry is None:
        cursor.execute("INSERT INTO history (user_id, song_id, liked, date, day_name) VALUES (?, ?, ?, ?, ?)", 
                       (user_id, song_id, liked, date, day_name))
    else:
        cursor.execute("UPDATE history SET liked = ? WHERE id = ?", (liked, history_entry[0]))

    conn.commit()
    conn.close()

# Function to process the CSV file
def process_csv(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    # Load the username from config.json
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        username = config.get('username')
        if not username:
            print("Error: Username not found in config.json.")
            return

    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            song_name = row['song'].strip()
            artist_name = row['artist'].strip()
            liked = row['liked'].strip().lower() == 'true'  # Convert "true" to Boolean
            date = row['date'].strip()

            insert_or_update_data(username, song_name, artist_name, liked, date)

# Main script
if __name__ == '__main__':
    csv_file_path = 'songs_data.csv'  # Change this to the path of your CSV file

    # Check if database exists, if not create it
    if not os.path.exists('songs_data.db'):
        create_db()

    # Process the CSV file
    process_csv(csv_file_path)

    print("Data processing complete.")
