from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.prepare_base_model import PrepareBaseModel
from CNNClassifier import logger



STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def base_model(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.base_model()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.exception(e)
        raise e