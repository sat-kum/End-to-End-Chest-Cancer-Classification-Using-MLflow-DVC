# End-to-End-Chest-Cancer-Classification-Using-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yam
3. Update params.yaml
4. update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py




## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/satkum/End-to-End-Chest-Cancer-Classification-Using-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=satkum \
MLFLOW_TRACKING_PASSWORD=3b54a2d6452213f49cae6ae2d020f903f50976c9 \
python script.py


Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/chest-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9353c5b10041d5c8edbcef0

```




### DVC cmd
    
1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

- Its Production Grade
- Trace all of your expriements
- Logging & taging your model


DVC 

- Its very lite weight for POC only
- lite weight expriements tracker
- It can perform Orchestration (Creating Pipelines)