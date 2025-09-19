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

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path : str
    matric_artifact: ClassificationMetricArtifact

    


