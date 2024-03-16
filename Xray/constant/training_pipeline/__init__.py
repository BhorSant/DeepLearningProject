from datetime import datetime
from typing import List

import torch
TIMESTAMP: datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

ARTIFACTS_DIR: str = "artifacts"

BUCKET_NAME: str = "xraylungings"

S3_DATA_FOLDER: str = "data"

CLASS_LABEL_1: str = "NORMAL"
CLASS_LABEL_2: str = "PNEUMONIA"

