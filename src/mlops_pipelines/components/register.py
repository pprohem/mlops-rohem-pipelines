from kfp import dsl
from google.cloud import aiplatform

@dsl.component(
    base_image="python:3.11",
    packages_to_install=["google-cloud-aiplatform"],
)
def register_op(
    model_dir: str,
    model_name: str,
    project_id: str,
    region: str,
    run_id: str,
    environment: str,
) -> str:
    aiplatform.init(
        project=project_id,
        location=region,
    )

    model = aiplatform.Model.upload(
        display_name=f"{model_name}-{environment}",
        artifact_uri=model_dir,
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-3:latest",
        labels={
            "model": model_name,
            "env": environment,
            "run_id": run_id,
        },
    )

    return model.resource_name
