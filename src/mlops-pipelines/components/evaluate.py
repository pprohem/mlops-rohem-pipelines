from kfp import dsl

@dsl.component
def evaluate_op(
    model: dsl.Input[dsl.Artifact],
) -> dsl.ContainerSpec:
    return dsl.ContainerSpec(
        image="python:3.11",
        command=["python", "-c"],
        args=[
            "print('Evaluating model')"
        ],
    )
