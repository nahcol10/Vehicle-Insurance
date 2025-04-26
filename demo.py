# from src.logger import logger
# logger.info("logger work successfully!!")

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import CustomException
# import sys
#
# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise CustomException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()