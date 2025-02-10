# This is to build our application as package

from setuptools import setup, find_packages
from typing import List
#if there are many packages then we can call this function
def get_requirements(file_name:str)->List[str]:
    '''
    this function will return the list of requiremnts
    '''
    requirements = []
    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."] 

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    description="ML Project",
    author="Sapana",
    author_email="sapanadhami1111@gmail.com",
    packages=find_packages(),  # Use find_packages directly
    install_requires= get_requirements("requirements.txt")
)