from setuptools import setup,find_packages
from typing import list,

#Declaring variables for setup functions 
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Ansh Verma"
DESCRIPTION="This is a first FSDS Nov batch Machine Learning project"
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->:List[str]:
    """
    Description: This function is going to return list of requirements
    mention in requirement.txt file

    return This function is going to return a list which contain name of libraries mentioned in requirement.txt file
    """
 with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #["housing"]
install_requires=get_requirements_list()

)

