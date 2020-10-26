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

CONTACT:
        Michael Taylor: mspacet@protonmail.com

"""

# ------ Importing required libraries ------ #

import pandas as pd
import numpy as np
import matploblib.pyplot as plt
import os
import logging

# ------ Configuration of logs ------ #

logging.basicConfig(filename='./project_logs.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)

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
