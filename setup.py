import pathlib
from setuptools import setup

ROOT=pathlib.Path(__file__).parent
README = (ROOT/'README.md').read_text()

setup(
    name="colorspacelib",
    version='0.9.8',
    author='Fredrick Pwol',
    author_email='fredpwol@gmail.com',
    url='https://github.com/Fredpwol/colorspacelib.git',
    description='A Python library for working and managing colors',
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT',

)