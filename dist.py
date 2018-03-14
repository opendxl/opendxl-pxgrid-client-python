from __future__ import absolute_import
from __future__ import print_function
import os
import subprocess

# pylint: disable=no-name-in-module, import-error
from distutils.dir_util import copy_tree, remove_tree
from distutils.file_util import copy_file, move_file
from distutils.core import run_setup
from distutils.archive_util import make_archive


# Run clean
import clean # pylint: disable=unused-import

print("Starting dist.\n")

VERSION = __import__('dxlciscopxgridclient').get_version()
RELEASE_NAME = "dxlciscopxgridclient-python-dist-" + str(VERSION)

DIST_PY_FILE_LOCATION = os.path.dirname(os.path.realpath(__file__))
DIST_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "dist")
DIST_DOCTMP_DIR = os.path.join(DIST_DIRECTORY, "doctmp")
SETUP_PY = os.path.join(DIST_PY_FILE_LOCATION, "setup.py")
DIST_LIB_DIRECTORY = os.path.join(DIST_DIRECTORY, "lib")
DIST_RELEASE_DIR = os.path.join(DIST_DIRECTORY, RELEASE_NAME)
SAMPLE_RELEASE_DIR = os.path.join(DIST_DIRECTORY, "sample")

# Remove the dist directory if it exists
if os.path.exists(DIST_DIRECTORY):
    print("\nRemoving dist directory: " + DIST_DIRECTORY + "\n")
    remove_tree(DIST_DIRECTORY, verbose=1)

print("\nMaking dist directory: " + DIST_DIRECTORY + "\n")
os.makedirs(DIST_DIRECTORY)

print("\nCalling sphinx-apidoc\n")
subprocess.check_call(["sphinx-apidoc",
                       "--force",
                       "--separate",
                       "--no-toc",
                       "--output-dir=" + DIST_DOCTMP_DIR,
                       os.path.join(DIST_PY_FILE_LOCATION, "dxlciscopxgridclient")])

print("\nCopying conf.py and sdk directory\n")
copy_file(os.path.join(DIST_PY_FILE_LOCATION, "doc", "conf.py"),
          os.path.join(DIST_DOCTMP_DIR, "conf.py"))
copy_tree(os.path.join(DIST_PY_FILE_LOCATION, "doc", "sdk"), DIST_DOCTMP_DIR)

print("\nCalling sphinx-build\n")
subprocess.check_call(["sphinx-build", "-b", "html", DIST_DOCTMP_DIR,
                       os.path.join(DIST_DIRECTORY, "doc")])

# Delete .doctrees
remove_tree(os.path.join(os.path.join(DIST_DIRECTORY, "doc"), ".doctrees"), verbose=1)
# Delete .buildinfo
os.remove(os.path.join(os.path.join(DIST_DIRECTORY, "doc"), ".buildinfo"))

print("\nMoving README.html\n")
move_file(os.path.join(DIST_DOCTMP_DIR, "README.html"), DIST_DIRECTORY)

print("\nDeleting doctmp directory\n")
remove_tree(DIST_DOCTMP_DIR)

print("\nRunning setup.py sdist\n")
run_setup(SETUP_PY,
          ["sdist",
           "--format",
           "zip",
           "--dist-dir",
           DIST_LIB_DIRECTORY])

print("\nRunning setup.py bdist_wheel\n")
run_setup(SETUP_PY,
          ["bdist_wheel",
           "--dist-dir",
           DIST_LIB_DIRECTORY,
           "--universal"])

print("\nCopying sample into dist directory\n")
copy_tree(os.path.join(DIST_PY_FILE_LOCATION, "sample"), SAMPLE_RELEASE_DIR)

print("\nCopying dist to " + DIST_RELEASE_DIR + "\n")
copy_tree(DIST_DIRECTORY, DIST_RELEASE_DIR)

print("\nRemoving build directory\n")
remove_tree(os.path.join(DIST_PY_FILE_LOCATION, "build"))

print("\nRemoving dxlciscopxgridclient.egg-info\n")
remove_tree(os.path.join(DIST_PY_FILE_LOCATION, "dxlciscopxgridclient.egg-info"))

print("\nMaking dist zip\n")
make_archive(DIST_RELEASE_DIR, "zip", DIST_DIRECTORY, RELEASE_NAME)

print("\nRemoving " + DIST_RELEASE_DIR + "\n")
remove_tree(DIST_RELEASE_DIR)
