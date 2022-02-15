"""
BITalino (R)evolution Python API

Setup for package installation.
"""

import sys

from setuptools import setup

if sys.version_info[:2] < (3, 7):
    raise RuntimeError("Python version >= 3.7 required.")


def readme():
    with open("README.md", "r") as f:
        description = f.read()
    return description


setup(
    name="bitalino",
    version="1.2.3",
    author="BITalinoWorld",
    author_email="bitalino@plux.info",
    url="http://www.bitalino.com/",
    py_modules=["bitalino"],
    description="revolution-python-api",
    long_description=readme(),
    download_url="https://github.com/BITalinoWorld/revolution-python-api",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    license="GNU GPL v3",
    keywords="BITalino, Physiological Computing, Biosignal, Physiological Signal",
    python_requires=">=3.7",
    install_requires=[
        "numpy==1.21.5",
        "pyserial==3.5",
        "pybluez @ git+https://github.com/pybluez/pybluez",
    ],
    zip_safe=False,
)
