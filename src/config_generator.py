"""
Configuration Loader Module

Responsibilities:
- Load YAML configuration files
- Provide centralized configuration access
"""

import yaml


class ConfigLoader:
    """
    Loads and manages YAML configuration files.
    """

    def __init__(self, config_path: str):
        self.config_path = config_path

    def load_config(self):
        """
        Load YAML configuration.
        """

        with open(self.config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        print("Configuration loaded successfully.")

        return config