from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
readme_file = path.join(here, 'README.md')
try:
    from m2r import parse_from_file
    long_description = parse_from_file(readme_file)
except ImportError:
    # m2r may not be installed in user environment
    with open(readme_file, encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='airtight',
    version='0.2.0',
    description='Components for scripts in python 3.6+',
    long_description=long_description,
    url='https://github.com/paregorios/airtight',
    author='Tom Elliott',
    author_email='tom.elliott@nyu.edu',
    license='LICENSE.txt',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='scripting',
    packages=['airtight'],
    python_requires='~=3.6'
)
