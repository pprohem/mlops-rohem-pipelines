from kfp import dsl
from kfp.dsl import Output, Artifact

@dsl.component(
    base_image="python:3.11",
)
def train_op(
    image_uri: str,
    dataset_uri: str,
    model: Output[Artifact],
):
    import subprocess

    subprocess.run(
        [
            "python",
            "train.py",
            "--dataset-uri", dataset_uri,
            "--model-dir", model.path,
        ],
        check=True,
    )
