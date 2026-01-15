from kfp.dsl import component
from google.cloud import aiplatform

@component
def register_model(model_dir: str, display_name: str):
    aiplatform.init()

    model = aiplatform.Model.upload(
        display_name=display_name,
        artifact_uri=model_dir,
        serving_container_image_uri="us-docker.pkg.dev/mlops-rohem/serving/sklearn:latest",
    )

    print(f"Modelo registrado: {model.resource_name}")
