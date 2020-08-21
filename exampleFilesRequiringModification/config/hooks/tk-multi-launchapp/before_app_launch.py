# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Before App Launch Hook

This hook is executed prior to application launch and is useful if you need
to set environment variables or run scripts as part of the app initialization.
"""

import sgtk
logger = sgtk.LogManager.get_logger(__name__)

msg = "\n\t--------------------\n\tbefore_app_launch.py\n\t--------------------"
print(msg)
logger.debug("{}".format(msg))


class BeforeAppLaunch(tank.Hook):
    """
    Hook to set up the system prior to app launch.
    """

    def execute(
        self, app_path, app_args, version, engine_name, software_entity=None, **kwargs
    ):
        # Load our framework
        fw = self.load_framework("tk-framework-example")

        # -= Option1 =-
        # Import our module via framework -> import module 
        # tk-framework-example\python\__init__.py
        #   from . import pythonfolderExampleModule
        pythonfolderExampleModule = fw.import_module("pythonfolderExampleModule")  
        # Display our module's message
        msg = pythonfolderExampleModule.returnMsg()
        logger.debug("\n\t{}".format(msg))

        # Demonstraing the missing import causes fw.import to fail
        try:
            pythonfolderExampleModule2 = fw.import_module("pythonfolderExampleModule2")
        except:
            logger.debug("\n\t{}".format(r"pythonfolderExampleModule2 import fails because it's missing the import statment in tk-framework-example\python\__init__.py"))
        # But also that we can import it directly (sys.path and PYTHONPATH statements in tk-framework-example\python\__init__.py)

        # -= Option2 =-
        # Implicit:  Import our module via standard importing.  Path added on framework init
        # Path added in tk-framework-example\framework.py
        import frameworkPythonPathModule
        msg = frameworkPythonPathModule.returnMsg()
        logger.debug("\n\t{}".format(msg))

        # -= Option3 =-
        # Explicit:  Import our module via standard importing
        # Path added in tk-framework-example\framework.py
        import frameworkPythonPathModule
        msg = frameworkPythonPathModule.returnMsg()
        logger.debug("\n\t{}".format(msg))

        