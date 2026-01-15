from kfp import dsl

from mlops_pipelines.components import (
    train_op,
    evaluate_op,
    register_op,
)

@dsl.pipeline(
    name="generic-training-pipeline",
)
def training_pipeline(
    project_id: str,
    region: str,
    model_name: str,
    image_uri: str,
    dataset_uri: str,
    run_id: str,
    environment: str,
):
    train = train_op(
        image_uri=image_uri,
        dataset_uri=dataset_uri,
    )

    evaluate = evaluate_op(
        model=train.outputs["model"],
    )

    register_op(
        model=evaluate.outputs["model"],
        model_name=model_name,
        project_id=project_id,
        region=region,
        run_id=run_id,
        environment=environment,
    )
