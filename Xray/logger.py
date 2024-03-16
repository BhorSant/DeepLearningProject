import logging
import os

from Xray.constant.training_pipeline import TIMESTAMP

LOG_FILE : str = f"log_{TIMESTAMP}.log"
logs_path = os.path.join(os.getcwd(),"logs",TIMESTAMP)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s : %(message)s]")
