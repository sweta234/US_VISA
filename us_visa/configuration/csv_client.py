import sys
import os
import pandas as pd

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import FILE_NAME


class CSVDataClient:
    """
    Class Name :   CSVDataClient
    Description :   This class loads data from a local CSV file 
                    instead of MongoDB, to keep project structure consistent.

    Output      :   Pandas DataFrame
    On Failure  :   raises an exception
    """

    def __init__(self, data_dir="notebook", file_name=FILE_NAME) -> None:
        try:
            self.data_path = os.path.join(data_dir, file_name)

            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"CSV file not found at path: {self.data_path}")

            logging.info(f"CSVDataClient initialized with file: {self.data_path}")

        except Exception as e:
            raise USvisaException(e, sys)

    def get_dataframe(self):
        """
        Loads CSV file into a pandas DataFrame.
        """
        try:
            df = pd.read_csv(self.data_path)
            logging.info(f"Data loaded successfully from {self.data_path}, shape: {df.shape}")
            return df
        except Exception as e:
            raise USvisaException(e, sys)
