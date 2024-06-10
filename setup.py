from setuptools import find_packages, setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    """
    This function returns list of requriments
    """

    reuqirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n") for req in requirments]


setup(
name='first_ml_project',
version='0.0.1'.
author='Ant',
author_email='antarikshpatel2002@gmail.com',
packages = find_packages(),
install_requires = get_requirments('requirments.txt')

)