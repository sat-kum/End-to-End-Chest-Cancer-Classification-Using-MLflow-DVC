import os
import zipfile
import gdown
import shutil
from src.CNNClassifier import logger
from src.CNNClassifier.utils.common import get_size
from src.CNNClassifier.entity.config_entity import DataIngestionConfig
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


os.environ['KAGGLE_USERNAME'] = ""
os.environ['KAGGLE_KEY'] = ""

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
     
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # file_id = dataset_url.split("/")[-2]
            # prefix = 'https://drive.google.com/uc?/export=download&id='
            # gdown.download(prefix+file_id,zip_download_dir)

            api.dataset_download_files(dataset_url, path=zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    
    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(os.path.join(self.config.local_data_file, "chest-ctscan-images.zip"), 'r') as zip_ref:
            all_files = zip_ref.namelist()
            specific_folders = ['normal', 'adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib']
            file_to_extract = [f for f in all_files if any(f.startswith(f"Data/train/{folder}") for folder in specific_folders)]
            for file in file_to_extract:
                zip_ref.extract(file, unzip_path)
        
        self.delete_unnecessary_folders(unzip_path, specific_folders)
        self.rename_folder(unzip_path, 'adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib', 'adenocarcinoma')

    def delete_unnecessary_folders(self, target_dir, keep_folders):
        data_train_path = os.path.join(target_dir, 'Data', 'train')
        for item in os.listdir(data_train_path):
            item_path = os.path.join(data_train_path, item)
            if os.path.isdir(item_path) and item not in keep_folders:
                shutil.rmtree(item_path)
                print(f"Deleted: {item_path}")

    def rename_folder(self, target_dir, old_name, new_name):
        old_path = os.path.join(target_dir, 'Data', 'train', old_name)
        new_path = os.path.join(target_dir, 'Data', 'train', new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} to {new_path}")
        else:
            print(f"Folder '{old_path}' does not exist.")
