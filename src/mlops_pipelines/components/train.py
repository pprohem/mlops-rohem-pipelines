from kfp import dsl

@dsl.component
def train_op(
    image_uri: str,
    dataset_uri: str,
) -> dsl.ContainerSpec:
    return dsl.ContainerSpec(
        image=image_uri,
        command=["python", "train.py"],
        args=[
            "--dataset-uri", dataset_uri,
        ],
    )
