"""
    This global_variables.py file contains all global variables that will be used for test
    configuration
"""
from pathlib import Path

# declare global variables
ROOT_DIR = Path(__file__).parent.resolve()
CONFIG_PATH = ROOT_DIR / 'config_files'