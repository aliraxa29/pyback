import json
import os


def get_db_url():
    """
    Returns the database URL for the application.
    """
    config_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config.json')
    
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"Configuration file not found at {config_file_path}")

    with open(config_file_path, 'r') as f:
        config = json.load(f)

    dbuser = config.get("dbuser")
    dbpassword = config.get("dbpassword")
    dbhost = config.get("dbhost")
    dbport = config.get("dbport")
    dbname = config.get("dbname")

    return f"mariadb+mariadbconnector://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}"