from unicodedata import name
from setuptools import setup, find_packages

# helps pytest finding the django project without 
# depending on location of manage.py 
# run: pip install --editable .
setup(name='rioacademy', version='1.0')


# if __name__ == '__main__':
#     setup(name='rioacademy', 
#         version='1.0', 
#         packages=find_packages())