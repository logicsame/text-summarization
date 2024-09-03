import os
import urllib.request as request
import zipfile
from src.textsummarizer.logging import logger
from src.textsummarizer.utils.common import get_size
from src.textsummarizer.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f'Download! with following info: \n{headers}')
        else:
            logger.info(f'File already exist of size: {get_size(Path(self.config.local_data_file))}')
            
            
            
    def extract_file(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as file :
            file.extractall(unzip_dir)   
    