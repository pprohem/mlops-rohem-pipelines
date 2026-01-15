from kfp import dsl
from kfp.dsl import Input, Output, Artifact

@dsl.component(
    base_image="python:3.11",
    packages_to_install=["google-cloud-aiplatform"],
)
def evaluate_op(
    image_uri: str,
    project_id: str,
    region: str,
    model: Input[Artifact],
    metrics: Output[Artifact],
):
    from google.cloud import aiplatform

    aiplatform.init(
        project=project_id,
        location=region,
        staging_bucket=f"gs://{project_id}-vertex-staging",
    )

    job = aiplatform.CustomJob(
        display_name="evaluate-job",
        worker_pool_specs=[
            {
                "machine_spec": {
                    "machine_type": "n1-standard-4",
                },
                "replica_count": 1,
                "container_spec": {
                    "image_uri": image_uri,
                    "command": ["python", "evaluate.py"],
                    "args": [
                        "--model-dir", model.path,
                        "--metrics-dir", metrics.path,
                    ],
                },
            }
        ],
    )

    job.run(sync=True)
