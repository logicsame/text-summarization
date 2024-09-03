from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.entity.config_entity import DataValidationConfig
from src.textsummarizer.conponents.data_validation import DataValiadtion


class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config  = ConfigurationManager()
        data_validataion_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validataion_config)
        data_validation.validate_all_files_exist()