# LAST.FM MUSIC ANALYTICS

## Description

**Last.fm Music Analytics** is a Python-based project that scrapes music data from the Last.fm website, processes it, and stores it in a SQLite database for analysis. The project consists of multiple components, including:

- **Web Scraping:** Uses Playwright to automate the scraping of a user’s listening history, including song names, artist names, liked status, and timestamps.  
**Note:** The time it takes for scraping depends on the size of your Last.fm data. It may take some time if you have a large music history.
- **Data Storage:** Uses SQLite to store and organize the scraped data into a structured database in **3rd Normal Form (3NF)** to ensure data integrity and reduce redundancy.
- **Data Processing:** Processes and cleans the scraped data, including handling missing years in dates, fixing relative time formats like “hours ago”, and inserting or updating records in the database.
- **Interactive Visualization:** Uses ipywidgets for interactive visualization of the data within Jupyter Notebooks, allowing users to explore their music data dynamically.

## Project Structure

- **`lastfm_scripting.py`**: The script that automates the process of logging into Last.fm, navigating the user library, and scraping data about songs and artists.
- **`csv_to_db.py`**: A Python script that processes a CSV file containing song data and inserts it into the SQLite database.
- **`interactive_data_aggregator.ipynb`**: A Jupyter notebook that allows users to interact with the music data, visualize trends, and perform data analysis in an interactive environment.
- **`config.json`**: A configuration file containing the Last.fm username, password, and scraping settings like the start and end page for the web scraping.


## Installation


Before running the project, make sure to install all required dependencies. You can install them directly from GitHub using pip:

```bash
pip install git+https://github.com/nose1317/Last.fm-Music-Analytics.git
```
Alternatively, if you'd prefer to install the dependencies locally, create a virtual environment and use pip to install the libraries from the requirements.txt file:

```bash
pip install -r requirements.txt
```
This will install all the necessary libraries, including Playwright, pandas, matplotlib, seaborn, ipywidgets, SQLite, and Jupyter.


Note:
If you're using Playwright for the first time, you may need to install the browser dependencies by running the following command:

```bash
python -m playwright install
```

## Locating the `config.json` File and Other Files After Installation

After installing the package with `pip install Last.fm-Music-Analytics`, the files will be located in your Python environment's `site-packages` directory.

You can find the root installation folder by running:

```bash
pip show Last.fm-Music-Analytics
```

This will display the location of the installed package. Look for the Location field, which will show the folder path.

For example:

```bash
Location: /path/to/python/site-packages
```

Once you find this folder, navigate to the directory where lfmma (the folder containing the config.json file) is located.

### Finding the config.json File
The config.json file is located inside the lfmma folder. You can access it by navigating to:

```bash
/path/to/python/site-packages/lfmma/config.json
```

This will print the full path to the config.json file within the installed package, allowing you to edit it for your credentials.

### Usage

#### Scraping Data
Configure your config.json with your Last.fm username and password.  
Run the scraping script (lastfm_scripting.py) to scrape music data and store it in a CSV file:

```bash
python lastfm_scripting.py
```

Note: The time it takes for scraping depends on the amount of data in your Last.fm account, and it may take some time to complete.

### Processing Data
Process the CSV file (songs_data.csv) and store it in the SQLite database by running the `csv_to_db.py` script:

```bash
python csv_to_db.py
```

Note: The data transformation process may also take time depending on the size and complexity of your CSV file, as it will be processed and inserted into the SQLite database for querying. The database is structured in 3rd Normal Form (3NF) to ensure optimal organization and minimize data redundancy.

### Interactive Data Analysis
Open `interactive_data_aggregator.ipynb` in Jupyter Notebook or JupyterLab.  
Use the provided widgets to visualize and interact with the scraped data.

### License
This project is licensed under the MIT License

GitHub: [nose1317](https://github.com/nose1317)

