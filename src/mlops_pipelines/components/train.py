from kfp import dsl
from kfp.dsl import Output, Artifact

@dsl.component(
    base_image="python:3.11",
    packages_to_install=["google-cloud-aiplatform"],
)
def train_op(
    image_uri: str,
    dataset_uri: str,
    project_id: str,
    region: str,
    model: Output[Artifact],
):
    """
    Executa o treino usando a imagem do time de DS.
    O container DEVE escrever o modelo em model.path.
    """
    from google.cloud import aiplatform

    aiplatform.init(
        project=project_id,
        location=region,
    )

    job = aiplatform.CustomJob(
        display_name="train-job",
        worker_pool_specs=[
            {
                "machine_spec": {
                    "machine_type": "e2-standard-4",
                },
                "replica_count": 1,
                "container_spec": {
                    "image_uri": image_uri,
                    "command": ["python", "train.py"],
                    "args": [
                        "--dataset-uri", dataset_uri,
                        "--model-dir", model.path,
                    ],
                },
            }
        ],
    )

    job.run(sync=True)
