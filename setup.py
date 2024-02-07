from setuptools import find_packages, setup
from pkg_resources import parse_requirements
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''To return the list of requirements'''
    requirements = parse_requirements(file_path, session=False)
    return [str(req) for req in requirements]

setup(
    name='mlproject',
    version='0.01',
    author='Poonam Ghode',
    author_email='pghode23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
