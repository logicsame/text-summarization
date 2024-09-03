from src.textsummarizer.conponents.data_tranformation import DataTransformation
from src.textsummarizer.config.configuration import ConfigurationManager

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()