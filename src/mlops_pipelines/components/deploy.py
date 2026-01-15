from kfp import dsl

@dsl.component
def deploy_op(
    model_name: str,
    project_id: str,
    region: str,
):
    return dsl.ContainerSpec(
        image="python:3.11",
        command=["python", "-c"],
        args=["print('Deploying model')"],
    )
