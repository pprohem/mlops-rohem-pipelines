from kfp import dsl
from google.cloud import aiplatform

@dsl.component(
    base_image="python:3.11",
    packages_to_install=["google-cloud-aiplatform"],
)
def deploy_op(
    model_resource_name: str,
    project_id: str,
    region: str,
    endpoint_name: str,
):
    aiplatform.init(
        project=project_id,
        location=region,
    )

    model = aiplatform.Model(model_resource_name)

    endpoint = aiplatform.Endpoint.create(
        display_name=endpoint_name,
    )

    model.deploy(
        endpoint=endpoint,
        machine_type="n1-standard-2",
    )
