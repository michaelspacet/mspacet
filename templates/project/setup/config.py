"""

PROJECT:
        Project

CODE:
        config.py

SUMMARY:
        Configuration settings for project

DOCS:
        None yet

LAST EDITED:
        26-10-2020 --> Creation
        02-02-2021 --> Proper configuration of logger

CONTACT:
        Michael Taylor: mspacet@protonmail.com

"""

# ------ Importing required libraries ------ #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import warnings
import logging

# ------ Display options and suppressing warnings ------ #

pd.set_option('display.max_columns', 250)
pd.set_option('display.max_rows', 250)
pd.options.mode.chained_assignment = None
warnings.simplefilter(action='ignore',
                      category=FutureWarning)

# ------ Configuration of logs ------ #

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler('logs.log'),
                              logging.StreamHandler()],
                    level=10)  # level options: 10 - debug, 20 - info, 30 - warning, 40 - error & 50 - critical

# ------ Setting up directories and defining variables ------ #

# Define cwd to be the current working directory
cwd = os.getcwd()

# Defining data paths
data_path = cwd + '/data/'
raw_data_path = data_path + 'raw/'
interim_data_path = data_path + 'interim/'
processed_data_path = data_path + 'processed/'

# Defining path to save plots in
plots_path = cwd + '/plots'

# Defining path where .sav files are located
models_path = cwd + '/models/'
