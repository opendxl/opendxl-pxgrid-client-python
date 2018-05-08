from __future__ import absolute_import
from __future__ import print_function
import os
# pylint: disable=no-name-in-module, import-error
from distutils.dir_util import remove_tree
from shutil import copyfile


def clean_dir(src_dir, directory):
    if os.path.exists(directory):
        print("Cleaning directory: " + directory + "\n")
        for f in os.listdir(directory):
            target_file = os.path.join(directory, f)
            if not os.path.isdir(target_file) and not f.lower().endswith(".py"):
                os.remove(os.path.join(directory, f))
        for f in os.listdir(src_dir):
            src_file = os.path.join(src_dir, f)
            if not os.path.isdir(src_file) and \
                    not(f.lower().endswith(".py") or f.lower().endswith(".pyc")):
                copyfile(src_file, os.path.join(directory, f))

print("Starting clean.\n")

DIST_PY_FILE_LOCATION = os.path.dirname(os.path.realpath(__file__))
DIST_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "dist")
CONFIG_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "config")
SAMPLE_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "sample")
CONFIG_SRC_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "dxlciscopxgridclient",
                                    "_config", "app")
SAMPLE_SRC_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "dxlciscopxgridclient",
                                    "_config", "sample")

# Remove the dist directory if it exists
if os.path.exists(DIST_DIRECTORY):
    print("Removing dist directory: " + DIST_DIRECTORY + "\n")
    remove_tree(DIST_DIRECTORY, verbose=1)

# Clean the config directory
clean_dir(CONFIG_SRC_DIRECTORY, CONFIG_DIRECTORY)

# Clean the samples directory
clean_dir(SAMPLE_SRC_DIRECTORY, SAMPLE_DIRECTORY)

# Clean .pyc files
print("Cleaning .pyc files")
for root, dirs, files in os.walk(DIST_PY_FILE_LOCATION):
    for source_file in files:
        full_path = os.path.join(root, source_file)
        if full_path.lower().endswith(".pyc"):
            os.remove(full_path)
