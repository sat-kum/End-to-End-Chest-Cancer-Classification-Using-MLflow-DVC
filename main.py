from CNNClassifier import logger
from src.CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.CNNClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline



logger.info("welcome to CNN classifier")



STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.dataingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.base_model()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX==========X")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.trainer()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e