def test_training_pipeline_import():
    from mlops_pipelines.pipelines.training import training_pipeline
    assert training_pipeline is not None
