from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path : str
    test_file_path : str

@dataclass
class DatavalidationArtifact:
    validation_status : bool 
    message : str     # ✅ correct spelling
    drift_report_file_path:str


