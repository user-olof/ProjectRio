from unicodedata import name
from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(name='rioacademy', 
        version='1.0', 
        packages=find_packages(),
        scripts=['manage.py'])