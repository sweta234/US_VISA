import pandas as pd

class CSVDataClient:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        """
        Reads the CSV file into a pandas DataFrame
        """
        return pd.read_csv(self.file_path)
