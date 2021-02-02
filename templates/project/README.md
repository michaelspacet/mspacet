--------
--------

Project Name
==============================

--------

Author: Michael Taylor  
Email: mspacet@protonmail.com  
Date: 02-02-2021   
Description: A short description of the project  
Repository:  

--------

Project Structure
------------

    ├── data (not tracked)
    │   ├── raw            -> Raw data with no pre-processing
    │   ├── interim        -> Any data that has been pre-processed
    │   ├── processed      -> Output data
    │
    ├── models             -> Folder to save any models that are built for future use
    │
    ├── notebooks          -> Jupyter notebooks
    │
    ├── plots              -> Used to save output plots
    │
    ├── setup              -> Contains configuration files for the pipeline
    │
    ├── src                -> Source code
    │   ├── build_data     -> Files required to get data and clean it
    │   ├── build_model    -> Files for making the model
    │   ├── evaluation     -> Evaluation scripts
    │
    ├── tests              -> Tests for src code
    │
    ├── Dockerfile         -> Dockerfile for building images
    ├── logs.log           -> Log file (not tracked)
    ├── README.md          -> Top level README file
    ├── requirements.txt   -> File with project's requirements
    ├── run.py             -> File used to run entire pipeline

--------

Setup
------------

- Create a virtual environment and activate it
- Python version: 3.6
- Install requirements using: `pip install -r requirements.txt`

--------

Run pipeline
------------

The command below should be run from `project` directory from your shell

**Run pipeline**

`python -m run.py`

--------  

Testing
------------

To run the tests: 

`python -m unittest discover tests`

--------  
--------
