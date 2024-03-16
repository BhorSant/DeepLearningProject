import sys

from Xray.exception import XRayException
from Xray.logger import logging
from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifacts_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

        def start_data_ingestion(self) -> DataIngestionArtifact:
            try:
                data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
                return data_ingestion.initiate_data_ingestion()

            except Exception as e:
                raise XRayException(e, sys)
            