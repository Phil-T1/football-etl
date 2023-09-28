"""Main application file."""

import os
import requests
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from requests.exceptions import RequestException


def read_dotenv() -> dict:
    """Read credentials from .env file, return as dict."""
    load_dotenv()
    env_list = [
        "API_KEY",
        "API_HOST",
        "LEAGUE_ID",
        "SEASON",
        "DB_NAME",
        "DB_USERNAME",
        "DB_PASSWORD",
        "DB_HOST",
        "DB_PORT",
    ]
    return {item: os.getenv(item) for item in env_list}
