from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import os
import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion.")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed.")
        print(dataingestionartifact)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate data validation.")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed.")
        print(datavalidationartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)