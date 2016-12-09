'''
BITalino (R)evolution Python API

Setup for package installation.
'''

from setuptools import setup

def readme():
    with open('README.rst', 'r') as f:
        description = f.read()
    return description


setup(
    name="bitalino",
    version="1.0",
    author="BITalinoWorld",
    author_email="bitalino@plux.info",
    url="http://www.bitalino.com/",
    py_modules=['bitalino'],
    description="revolution-python-api",
    long_description=readme(),
    download_url="https://github.com/BITalinoWorld/revolution-python-api",
    classifiers= ['License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                  'Programming Language :: Python',
                  'Topic :: Scientific/Engineering',
                  'Topic :: Software Development :: Libraries'],
    license= "GNU GPL v3",
    keywords='BITalino, Physiological Computing, Biosignal, Physiological Signal',
    install_requires=[],
    zip_safe=False
)
