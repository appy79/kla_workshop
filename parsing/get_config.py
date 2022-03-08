import csv, yaml, os
from dotenv import load_dotenv


load_dotenv()


def current_config():
    config_file_path = os.environ.get("CONFIG_FILE")

    with open(config_file_path) as f:
        config = list(yaml.load_all(f, Loader=yaml.FullLoader))

    return config
