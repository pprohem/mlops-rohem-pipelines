from kfp import dsl
from kfp.dsl import Input, Artifact

@dsl.component(
    base_image="python:3.11",
    packages_to_install=["google-cloud-aiplatform"],
)
def register_op(
    model: Input[Artifact],
    model_name: str,
    project_id: str,
    region: str,
    run_id: str,
    environment: str,
) -> str:
    from google.cloud import aiplatform

    aiplatform.init(
        project=project_id,
        location=region,
    )

    uploaded_model = aiplatform.Model.upload(
        display_name=f"{model_name}-{environment}",
        artifact_uri=model.path,
        serving_container_image_uri=(
            "us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-3:latest"
        ),
        labels={
            "model": model_name,
            "env": environment,
            "run_id": run_id,
        },
    )

    return uploaded_model.resource_name
