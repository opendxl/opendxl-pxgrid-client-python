import os
from setuptools import setup
import distutils.command.sdist

import setuptools.command.sdist

# Patch setuptools' sdist behaviour with distutils' sdist behaviour
setuptools.command.sdist.sdist.run = distutils.command.sdist.sdist.run

version_info = {}
cwd=os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, "dxlciscopxgridclient", "_version.py")) as f:
    exec(f.read(), version_info)

dist = setup(
    # Package name:
    name="dxlciscopxgridclient",

    # Version number:
    version=version_info["__version__"],

    # Requirements
    install_requires=[
        "dxlbootstrap",
        "dxlclient"
    ],

    # Package author details:
    author="",

    # License
    license="",

    # Keywords
    keywords=[],

    # Packages
    packages=[
        "dxlciscopxgridclient",
    ],

    # Details
    url="",

    description="",

    long_description=open('README').read(),

    classifiers=[
        "Programming Language :: Python"
    ],
)
