import csv, yaml, os
from dotenv import load_dotenv
import logging, csv

load_dotenv()
config_file_path = os.environ.get("CONFIG_FILE")


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
filename = config_file_path[-16:-5]
handler = logging.FileHandler(filename + ".log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s;%(message)s")
formatter.default_msec_format = "%s.%06d"
handler.setFormatter(formatter)
logger.addHandler(handler)


def current_config():

    with open(config_file_path) as f:
        config = list(yaml.load_all(f, Loader=yaml.FullLoader))

    return config
