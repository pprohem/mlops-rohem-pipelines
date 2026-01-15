from kfp import dsl

def evaluate_op(
    image_uri: str,
    model_dir: str,
):
    return dsl.ContainerSpec(
        image=image_uri,
        command=["python", "evaluate.py"],
        args=[
            "--model-dir", model_dir,
        ],
    )
