import sys
import numpy as np
import pandas as pd
from imblearn.combine import SMOTEENN
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, PowerTransformer, StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer

from us_visa.constants import TARGET_COLUMNS , SCHEMA_FILE_PATH, CURRENT_YEAR

from us_visa.entity.config_entity import DataTransformationConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, DatavalidationArtifact
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.utils.main_utils import save_object, save_numpy_array_data, read_yaml_file, drop_columns

from us_visa.entity.estimator import TargetValueMapping
import os

class DataTransformation:
    def __init__(self, 
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_transformation_config: DataTransformationConfig,
                 data_validation_artifact: DatavalidationArtifact):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_config = data_transformation_config
            self.data_validation_artifact = data_validation_artifact
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise USvisaException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise USvisaException(e, sys)

    def get_data_transformer_object(self) -> Pipeline:
        logging.info("Entered get_data_transformer_object method of DataTransformation class")

        try:
            oh_transformer = OneHotEncoder(handle_unknown="ignore")
            numeric_transformer = StandardScaler()

            categorical_cols = self._schema_config['categorical_columns']
            numeric_cols = self._schema_config['numerical_columns']

            preprocessor = ColumnTransformer(
                transformers=[
                    ("OneHotEncoder", oh_transformer, categorical_cols),
                    ("StandardScaler", numeric_transformer, numeric_cols)
                ]
            )

            return preprocessor

        except Exception as e:
            raise USvisaException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            if not self.data_validation_artifact.validation_status:
                 raise Exception(self.data_validation_artifact.message)
            
            logging.info("Starting data transformation")
            
            preprocessor = self.get_data_transformer_object()
            
            # Load train and test data
            train_df = DataTransformation.read_data(self.data_ingestion_artifact.trained_file_path)
            test_df = DataTransformation.read_data(self.data_ingestion_artifact.test_file_path)

              # Split input and target features
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMNS], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMNS]

            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMNS], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMNS]

            # Drop unnecessary columns (if defined in schema)
            drop_cols = self._schema_config['drop_columns']
            input_feature_train_df = drop_columns(df=input_feature_train_df, cols=drop_cols)
            input_feature_test_df = drop_columns(df=input_feature_test_df, cols=drop_cols)

            # Target column is already 0 and 1, no mapping needed
            logging.info("Target column already numeric (0/1), skipping mapping")

            # Apply preprocessing
            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor.transform(input_feature_test_df)

            # Handle imbalance using SMOTEENN
            smt = SMOTEENN(sampling_strategy="minority")
            input_feature_train_final, target_feature_train_final = smt.fit_resample(
            input_feature_train_arr, target_feature_train_df)
             
            input_feature_test_final, target_feature_test_final = smt.fit_resample(
            input_feature_test_arr, target_feature_test_df)

            # Combine features and targets  
            train_arr = np.c_[input_feature_train_final, np.array(target_feature_train_final)]
            test_arr = np.c_[input_feature_test_final, np.array(target_feature_test_final)]

            
            # ✅ Ensure directories exist before saving
            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_train_file_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_test_file_path), exist_ok=True)
            #os.makedirs(os.path.dirname(self.data_transformation_config.transformed_object_file_path), exist_ok=True)

             # Save preprocessor object and numpy arrays
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor)
            np.save(self.data_transformation_config.transformed_train_file_path, train_arr)
            np.save(self.data_transformation_config.transformed_test_file_path, test_arr)

            logging.info("Data transformation completed successfully")



           # Return artifact
            return DataTransformationArtifact(
            transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
            transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
            transformed_test_file_path=self.data_transformation_config.transformed_test_file_path)
        except Exception as e:
            raise USvisaException(e, sys)
