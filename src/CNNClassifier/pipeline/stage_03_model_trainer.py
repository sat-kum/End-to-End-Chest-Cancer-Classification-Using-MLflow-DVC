from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_trainer import Training
from CNNClassifier import logger



STAGE_NAME = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def trainer(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.exception(e)
        raise e
        