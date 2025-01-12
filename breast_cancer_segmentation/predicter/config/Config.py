import os
from hydra import compose, initialize


class Config:
    def __init__(self):
        self.storage_mode = os.getenv("STORAGE_MODE", "local")
        with initialize(version_base=None, config_path="."):
            config = compose(config_name="config.yaml")
            self.model_path = os.getenv("MODEL_PATH", config.model_path)
            self.model_repository = config.model_repository
        self.device = os.getenv("DEVICE", "cpu")
