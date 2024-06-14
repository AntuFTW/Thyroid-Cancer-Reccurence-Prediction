from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirments(file_path:str)->List[str]:
    """
    This function returns list of requriments
    """

    reuqirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)


setup(
name='first_ml_project',
version='0.0.1',
author='Ant',
author_email='antarikshpatel2002@gmail.com',
packages = find_packages(),
install_requires = get_requirments('requirments.txt')
)