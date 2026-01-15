from dataclasses import dataclass

@dataclass
class TrainingContract:
    project_id: str
    region: str
    model_name: str
    image_uri: str
    dataset_uri: str
    run_id: str
    environment: str
