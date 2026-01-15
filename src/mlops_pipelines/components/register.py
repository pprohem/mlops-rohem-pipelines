from kfp import dsl

@dsl.component
def register_op(
    model: dsl.Input[dsl.Artifact],
    model_name: str,
    project_id: str,
    region: str,
    run_id: str,
    environment: str,
) -> dsl.ContainerSpec:
    return dsl.ContainerSpec(
        image="python:3.11",
        command=["python", "-c"],
        args=[
            "print('Registering model')"
        ],
    )
