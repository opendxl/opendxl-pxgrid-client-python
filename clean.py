import os
from distutils.dir_util import remove_tree
from shutil import copyfile


def clean_dir(directory):
    if os.path.exists(directory):
        print("Cleaning directory: " + directory + "\n")
        for f in os.listdir(directory):
            if not os.path.isdir(os.path.join(directory, f)) \
                    and not f.lower().endswith(".dist") and not f.lower().endswith(".py"):
                os.remove(os.path.join(directory, f))
        for f in os.listdir(directory):
            if not os.path.isdir(f) and f.lower().endswith(".dist"):
                copyfile(os.path.join(directory, f), os.path.join(directory, f[:-5]))


print("Starting clean.\n")

DIST_PY_FILE_LOCATION = os.path.dirname(os.path.realpath(__file__))
DIST_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "dist")
CONFIG_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "config")
SAMPLE_DIRECTORY = os.path.join(DIST_PY_FILE_LOCATION, "sample")

# Remove the dist directory if it exists
if os.path.exists(DIST_DIRECTORY):
    print("Removing dist directory: " + DIST_DIRECTORY + "\n")
    remove_tree(DIST_DIRECTORY, verbose=1)

# Clean the config directory
clean_dir(CONFIG_DIRECTORY)

# Clean the samples directory
clean_dir(SAMPLE_DIRECTORY)

# Clean .pyc files
print("Cleaning .pyc files")
for root, dirs, files in os.walk(DIST_PY_FILE_LOCATION):
    for file in files:
        full_path = os.path.join(root, file)
        if full_path.lower().endswith(".pyc"):
            os.remove(full_path)
