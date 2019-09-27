# pylint: disable=no-member, no-name-in-module, import-error

from __future__ import absolute_import
import glob
import os
import distutils.command.sdist
import distutils.log
import subprocess
from setuptools import Command, setup
import setuptools.command.sdist

# Patch setuptools' sdist behaviour with distutils' sdist behaviour
setuptools.command.sdist.sdist.run = distutils.command.sdist.sdist.run

VERSION_INFO = {}
CWD = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(CWD, "dxlciscopxgridclient", "_version.py")) as f:
    exec(f.read(), VERSION_INFO)  # pylint: disable=exec-used


class LintCommand(Command):
    """
    Custom setuptools command for running lint
    """
    description = 'run lint against project source files'
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        self.announce("Running pylint for library source files and tests",
                      level=distutils.log.INFO)
        subprocess.check_call(["pylint", "dxlciscopxgridclient"] +
                              glob.glob("*.py"))
        self.announce("Running pylint for samples", level=distutils.log.INFO)
        subprocess.check_call(["pylint"] + glob.glob("sample/*.py") +
                              glob.glob("sample/**/*.py") +
                              ["--rcfile", ".pylintrc.samples"])


class CiCommand(Command):
    """
    Custom setuptools command for running steps that are performed during
    Continuous Integration testing.
    """
    description = 'run CI steps (lint, test, etc.)'
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        self.run_command("lint")

TEST_REQUIREMENTS = ["pylint<=2.3.1"]

DEV_REQUIREMENTS = TEST_REQUIREMENTS + ["sphinx"]

setup(
    # Package name:
    name="dxlciscopxgridclient",

    # Version number:
    version=VERSION_INFO["__version__"],

    # Requirements
    install_requires=[
        "dxlbootstrap>=0.2.0",
        "dxlclient>=4.1.0.184"
    ],

    tests_require=TEST_REQUIREMENTS,

    extras_require={
        "dev": DEV_REQUIREMENTS,
        "test": TEST_REQUIREMENTS
    },

    # Package author details:
    author="McAfee LLC",

    # License
    license="Apache License 2.0",

    # Keywords
    keywords=['opendxl', 'dxl', 'mcafee', 'client', 'cisco', 'pxgrid'],

    # Packages
    packages=[
        "dxlciscopxgridclient",
        "dxlciscopxgridclient._config",
        "dxlciscopxgridclient._config.sample"],

    package_data={
        "dxlciscopxgridclient._config.sample" : ['*']},

    # Details
    url="http://www.mcafee.com",

    description="Cisco pxGrid DXL client library",

    long_description=open('README').read(),

    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',

    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],

    cmdclass={
        "ci": CiCommand,
        "lint": LintCommand
    }
)
