from kfp import dsl
from kfp.dsl import Input, Output, Artifact

@dsl.component(
    base_image="python:3.11",
)
def evaluate_op(
    image_uri: str,
    model: Input[Artifact],
    metrics: Output[Artifact],
):
    import subprocess

    subprocess.run(
        [
            "python",
            "evaluate.py",
            "--model-dir", model.path,
            "--metrics-dir", metrics.path,
        ],
        check=True,
    )
