#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# hyde build script - searches the current directory and its
# ancestors for a hyde root directory. If found, it executes
# hyde -g to build the site.
#
# Author: mt@thiguten.de
#

import os
import sys
import subprocess


def check_if_hyde_dir(path):
    """
    check if this directory is a hyde project root directory.
    This is done by looking for a file named 'settings.py'
    """
    files = os.listdir(path)
    return "settings.py" in files

path = os.path.abspath(".")
sys.stderr.write("Running hyde-build.py in %s\n" % path)
found = check_if_hyde_dir(path)

while not found:
    path = os.path.abspath(os.path.join(path, ".."))
    if path == os.sep:
        # arrived at root
        break

    found = check_if_hyde_dir(path)


if not found:
    sys.stderr.write("No hyde settings.py found in tree.\n\n")
    sys.exit(2)

hyde_ve_dir = os.path.join(os.getenv("HOME"), 've/hyde/')

# get hyde python interpreter
py = os.path.join(hyde_ve_dir, 'bin/python')
# get hyde script
hyde = os.path.join(hyde_ve_dir, 'hyde/hyde.py')

# execute hyde build
print "Running hyde build in " + path
if len(sys.argv) > 1:
    # run with arguments provided by caller
    ret = subprocess.call([py, hyde] + sys.argv[1:], cwd=path)
else:
    ret = subprocess.call([py, hyde, "-g"], cwd=path)

sys.exit(ret)





