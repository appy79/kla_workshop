import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler("parsing.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s;%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
