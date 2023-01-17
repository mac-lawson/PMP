
"""v1OS.py: The main file for the project, just gets the APPDATA info"""

__author__      = "Mac Lawson"
__copyright__   = "Copyright 2023"

import os 

def get_app_data():
    # Define the path to the application data folder
    app_data_path = os.path.join(os.environ['APPDATA'])

    # Print the contents of the folder
    for item in os.listdir(app_data_path):
        return(item)

def get_system_info():
    # Get system name
    system_name = os.name

    # Get system release information
    release_info = " ".join(os.uname())

    # Get current working directory
    cwd = os.getcwd()

    # Get environment variables
    env_vars = os.environ

    # Print the information
    return("System name: ", system_name)
    return("System release information: ", release_info)
    return("Current working directory: ", cwd)
    return("Environment variables: ", env_vars)