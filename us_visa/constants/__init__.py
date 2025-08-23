import os
from datetime import date

# Path to dataset inside notebook folder
DATA_FILE_PATH = os.path.join("notebook", "usvisa.csv")


PIPELINE_NAME : str = 'usvisa'

ARTIFACT_DIR : str = 'artifact'

FILE_NAME = "Churn_Modelling.csv" 

MODEL_FILE_NAME = 'Model.pkl'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

"""
Data ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME : str = "us_visa"

DATA_INGESTION_DIR_NAME : str = "data ingestion"

DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"

DATA_INGESTION_INGESTED_DIR = str = 'ingested'

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2

