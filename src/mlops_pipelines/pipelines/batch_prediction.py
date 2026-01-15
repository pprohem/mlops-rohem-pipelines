from kfp import dsl

@dsl.pipeline(
    name="generic-batch-prediction-pipeline",
)
def batch_prediction_pipeline(
    project_id: str,
    region: str,
    model_name: str,
    input_uri: str,
    output_uri: str,
):
    pass
