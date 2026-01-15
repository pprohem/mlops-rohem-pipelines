from kfp import dsl

def train_op(
    image_uri: str,
    dataset_uri: str,
):
    return dsl.ContainerSpec(
        image=image_uri,
        command=["python", "train.py"],
        args=[
            "--dataset-uri", dataset_uri,
        ],
    )
