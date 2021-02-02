"""

PROJECT:
        Project

CODE:
        run.py

SUMMARY:
        File that when executed will run the project pipeline

DOCS:
        None yet

LAST EDITED:
        02-02-2021 --> Creation

CONTACT:
        Michael Taylor: mspacet@protonmail.com

"""

from setup.config import *

logging.info('---------- RUNNING: run.py ----------')

RUN = {'get_new_data': True,
       'clean_data': False,
       'train_model': False,
       'make_predictions': False,
       'evaluate_predictions': False}

if RUN['get_new_data']:
    pass

logging.info('---------- FINISHED: run.py ----------')
