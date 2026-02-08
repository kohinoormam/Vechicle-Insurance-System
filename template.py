#os module- functions for interacting with the OS
#pathlib.Path-an Obj Or approach to handle file system paths.
import os
from pathlib import Path
#src will be the root folder for your project’s source code.
#All main Python modules will be created under this folder. 
project_name = "src"
#list of files that will be under src
#Includes Python modules (.py), configuration files (.yaml), 
#app entry points (app.py, demo.py), Docker files, and setup files.
#eg:components is folder name and __init__.py is file name
#f allows dynamic path based on project folder

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    #This will be created outside src
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]
#Convert each file path to a Path object for easier manipulation.
#Split the path into:
#filedir → The folder/directory of the file
#filename → The file name

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

#If the file has a directory (filedir is not empty), create it using os.makedirs().
#exist_ok=True → Won’t raise an error if the directory already exists.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
 #Checks if the file doesn’t exist OR is empty.
#Creates an empty file with open(filepath, "w").       
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")