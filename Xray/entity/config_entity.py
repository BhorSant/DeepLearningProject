import os
from dataclasses import dataclass
from torch import device
from Xray.constant.training_pipeline import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder: str =  S3_DATA_FOLDER
        self.bucket_name: str = BUCKET_NAME
        self.artifacts_dir: str = os.path.join(ARTIFACTS_DIR,TIMESTAMP)
        self.data_path: str = os.path.join(self.artifacts_dir, self.s3_data_folder)
        self.device: device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        