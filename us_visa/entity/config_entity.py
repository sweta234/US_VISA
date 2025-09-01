import os

from us_visa.constants import * 
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP : str = datetime.now().strftime("%M_%d_%Y_%H_%M_%S")  # pyright: ignore[reportInvalidTypeForm]

@dataclass
class TrainingPipelineConfig:
    pipeline_name : str = PIPELINE_NAME # type: ignore
    artifact_dir : str = os.path.join(ARTIFACT_DIR, TIMESTAMP) # type: ignore
    timestamp : str = TIMESTAMP # type: ignore


training_Pipeline_Config  = TrainingPipelineConfig =   TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_Pipeline_Config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name: str = DATA_INGESTION_COLLECTION_NAME

#local_data_file: str = os.path.join("notebook", FILE_NAME)

@dataclass
class Datavalidationconfig:
    data_validation_dir : str = os.path.join(training_Pipeline_Config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    drift_report_file_path : str = os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR,
                                               DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
    
