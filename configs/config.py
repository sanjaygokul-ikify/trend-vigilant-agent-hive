import logging
from typing import Dict

logging.basicConfig(level=logging.INFO)

class Config:
    def __init__(self, config_dict: Dict[str, str]):
        self.config_dict = config_dict

    def get_config(self, key: str) -> str:
        try:
            return self.config_dict[key]
        except KeyError:
            logging.error(f'Config key {key} not found')
            raise ValueError(f'Config key {key} not found')

    def set_config(self, key: str, value: str) -> None:
        self.config_dict[key] = value