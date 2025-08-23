from us_visa.configuration.csv_data_connection import CSVDataClient 
from us_visa.exception import USvisaException
import pandas as pd
import numpy as np
import sys


class USvisaData:
    """
    This class helps to export dataset from local folder (not from MongoDB).
    """

    def __init__(self, folder_path: str = "notebook/data"):
        try:
            self.csv_client = CSVDataClient(folder_path=folder_path)
        except Exception as e:
            raise USvisaException(e, sys)

    def export_file_as_dataframe(self, file_name: str) -> pd.DataFrame:
        """
        Load a dataset file as pandas DataFrame
        """
        try:
            df = self.csv_client.load_file_as_dataframe(file_name)

            # Clean up if needed (same as Mongo version)
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e, sys)
