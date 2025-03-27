from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requtrements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        requirements=[req.replace('\n',"")for req  in requirements]
    return requirements


setup(

name="Customer Satisfaction Prediction",
version='0.0.1',
author='Rajat Sharma',
author_email="galyanrajat@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")

)


