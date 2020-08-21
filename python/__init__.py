# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

# Requried to allow the fw.import_module work
import os
import sys
from . import pythonfolderExampleModule

# Add the framework's/python folder to pythonpath
frameworkPythonDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(frameworkPythonDir)
os.environ["PYTHONPATH"] = "{};{}".format(os.environ["PYTHONPATH"], frameworkPythonDir)
