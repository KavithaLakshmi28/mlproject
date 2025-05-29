from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DASH = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    # Remove any whitespace and comments
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    # If '-e .' is in the requirements, remove it
    if HYPHEN_E_DASH in requirements:
        requirements.remove(HYPHEN_E_DASH)
    
    return requirements
    

setup(
    name='mlproject',
    version='0.0.1',    
    author='Kavitha', 
    author_email='kavithalkshm67@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )