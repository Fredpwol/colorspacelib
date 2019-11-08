import pathlib
from setuptools import setup

ROOT=pathlib.Path(__file__).parent
README = (ROOT/'README.md').read_text()

setup(
    name="colorsapcelib",
    version='0.9.6',
    author='Fredrick Pwol',
    author_email='fredpwol@gmail.com',
    url='https://github.com/Fredpwol/colorspacelib.git',
    description='A Python color library That easier to work with',
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT',

)