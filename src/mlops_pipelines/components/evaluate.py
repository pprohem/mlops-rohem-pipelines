from kfp.dsl import Input, Artifact

@dsl.component
def evaluate_op(
    image_uri: str,
    model: Input[Artifact],
    metrics: Output[Artifact],
):
    return dsl.ContainerSpec(
        image=image_uri,
        command=["python", "evaluate.py"],
        args=[
            "--model-dir", model.path,
            "--metrics-dir", metrics.path,
        ],
    )
