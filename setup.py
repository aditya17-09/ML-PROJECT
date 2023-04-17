from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS FROM THE GIVEN FILE'''
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
 
        return requirements
    
setup(
    name='ML PROJECT',
    version="0.0.1",
    author="ADITYA GAUTAM",
    author_email="aditya.kumar2020@vitbhopal.ac.in",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)