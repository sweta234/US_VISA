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
    data_ingestion_dir: str = os.path.join(training_Pipeline_Config.artifact_dir, DATA_INGESTION_DIR_NAME) # type: ignore
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME) # type: ignore
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME) # type: ignore
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME) # type: ignore
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name: str = DATA_INGESTION_COLLECTION_NAME # type: ignore

#local_data_file: str = os.path.join("notebook", FILE_NAME)

@dataclass
class Datavalidationconfig:
    data_validation_dir : str = os.path.join(training_Pipeline_Config.artifact_dir, DATA_VALIDATION_DIR_NAME) # type: ignore
    drift_report_file_path : str = os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR, # type: ignore
                                               DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
    


@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_Pipeline_Config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME) # type: ignore
    transformed_train_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, # type: ignore
                                                    TRAIN_FILE_NAME.replace("csv", "npy"))
    transformed_test_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, # type: ignore
                                                   TEST_FILE_NAME.replace("csv", "npy"))
    transformed_object_file_path: str = os.path.join(data_transformation_dir, # type: ignore
                                                     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     PREPROCESSING_OBJECT_FILE_NAME)


@dataclass
class ModelTrainerConfig:
    model_trainer_dir : str = os.path.join(training_Pipeline_Config.artifact_dir, MODEL_TRAINER_DIR_NAME) # type: ignore
    trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_FILE_NAME) # type: ignore
    expected_accuracy : float = MODEL_TRAINER_EXPECTED_SCORE
    model_config_file_path : str = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH # type: ignore

    

    
