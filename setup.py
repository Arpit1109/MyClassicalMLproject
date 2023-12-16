# It is responsible for creating my machine learning application as a package and that can be installed in your projects 

from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='MyClassicalMLProject',
    version='1.0.0',
    description='A project that is based on Classical ML',
    author='Arpit Agrahari',
    author_email='arpitagrahari19@email.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)