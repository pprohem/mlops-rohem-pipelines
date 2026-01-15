from kfp import dsl

@dsl.pipeline(
    name="generic-retraining-pipeline",
)
def retraining_pipeline(
    project_id: str,
    region: str,
    model_name: str,
):
    pass
