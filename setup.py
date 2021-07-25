from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'A basic CLI program to play battleship against the computer'

setup(
    name='cliBattleship',
    version=VERSION,
    author='Tyson Van Patten',
    author_email='tyson@descriptdata.com',
    url='https://github.com/tvanpat/cli-battleship',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[]
)
