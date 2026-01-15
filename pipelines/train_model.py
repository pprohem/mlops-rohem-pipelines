from kfp import dsl
from google_cloud_pipeline_components.v1.custom_job import CustomTrainingJobOp
from pipelines.validate_model import validate_model
from pipelines.register_model import register_model

@dsl.pipeline(name="generic-train-pipeline")
def pipeline(
    image_uri: str,
    model_display_name: str,
    min_r2: float,
    max_mae: float,
):
    # STEP 1 — Treino (container do DS)
    train = CustomTrainingJobOp(
        project="mlops-rohem",
        location="us-central1",
        display_name=model_display_name,
        base_output_directory="gs://mlops-cd4ml-trial/training",
        worker_pool_specs=[{
            "machine_spec": {"machine_type": "e2-standard-4"},
            "replica_count": 1,
            "container_spec": {
                "image_uri": image_uri,
                "command": ["python", "train.py"],
            },
        }],
    )

    # STEP 2 — Gate de qualidade
    validate_model(
        model_dir=train.outputs["model_dir"],
        min_r2=min_r2,
        max_mae=max_mae,
    )

    # STEP 3 — Registro do modelo
    register_model(
        model_dir=train.outputs["model_dir"],
        display_name=model_display_name,
    )
