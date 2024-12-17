# lastfm_music_analytics/__init__.py

# Import essential functions from modules
from .lastfm_scripting import scrape_lastfm
from .csv_to_db import process_csv, create_db

# You can also add versioning
__version__ = "0.1.0"

# Initialize other necessary setups if required (e.g., config loading)
