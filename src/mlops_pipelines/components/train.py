from kfp import dsl
from kfp.dsl import Output, Artifact

@dsl.component
def train_op(
    image_uri: str,
    dataset_uri: str,
    model: Output[Artifact],
):
    return dsl.ContainerSpec(
        image=image_uri,
        command=["python", "train.py"],
        args=[
            "--dataset-uri", dataset_uri,
            "--model-dir", model.path,
        ],
    )
