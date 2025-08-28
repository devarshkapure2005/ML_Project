# It helps to build your ML project and import it as a package
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(requirements_path: str) -> List[str]:
    """This function will return the list of requirements"""
    with open(requirements_path) as requirement_file:
        requirements = requirement_file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name="ml_project",
    version="0.1.0",
    author="Devarsh",
    author_email="devilsxiangviper@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(requirements_path="requirements.txt")
    )