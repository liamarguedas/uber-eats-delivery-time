#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'uber-eats-delivery-time-prediction'
DESCRIPTION = "Delivery time prediction system utilizing deep learning"
URL = "https://github.com/liamarguedas/uber-eats-delivery-time"
EMAIL = "iliamftw2013@gmail.com"
AUTHOR = "liamarguedas"
REQUIRES_PYTHON = ">=3.6.0"

long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary.
about = {}

ROOT_DIR = Path(__file__).resolve().parent

REQUIREMENTS_DIR = ROOT_DIR / 'requirements'

PACKAGE_DIR = ROOT_DIR / 'uber-eats-delivery-time'

with open(PACKAGE_DIR / "VERSION") as f:

    _version = f.read().strip()

    about["__version__"] = _version


# Requirements
def list_reqs(fname = "requirements.txt"):

    with open(REQUIREMENTS_DIR / fname) as fd:
        
        return fd.read().splitlines()

# Where the magic happens:
setup(
    name = NAME,
    version = about["__version__"],
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = AUTHOR,
    author_email = EMAIL,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(exclude=("tests",)),
    package_data = {"uber-eats-delivery-time": ["VERSION"]},
    install_requires = list_reqs(),
    extras_require = {},
    include_package_data = True,
    license = "BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)