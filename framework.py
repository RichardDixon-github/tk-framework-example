# This file is based on templates provided and copyrighted by Autodesk, Inc.
# This file has been modified by Epic Games, Inc. and is subject to the license
# file included in this repository.

"""
Framework containing PySide2 distributions for the Unreal engine

Because Unreal does not include PySide2/Qt distributions but does use its own
version of Python, we have to distribute full versions for the engine to function.
"""

import sgtk
import sys
import os


class ExampleFramework(sgtk.platform.Framework):

    ##########################################################################################
    # init and destroy

    def init_framework(self):
        # Create a debug message visible from the shotgun console
        msg = "\ttk-framework-example -> framework.py\n\tExampleFramework Class initialized"
        self.log_debug("%s\n{}".format(msg) % self)

        # Demonstrate importing module relative to framework.py
        frameworkPythonFolder = \
            os.path.join(self.disk_location, "frameworkPythonFolder")
        sys.path.append(frameworkPythonFolder)
        import frameworkPythonModule
        msg = frameworkPythonModule.returnMsg()
        self.log_debug("%s{}".format(msg) % self)

        # Demonstrate importing module relative to framework.py 
        #  and making it available in a decendant process
        frameworkPythonPathFolder = \
            os.path.join(self.disk_location, "frameworkPythonPathFolder")
        sys.path.append(frameworkPythonPathFolder)
        # Adding to pythonpath here makes the folder available in the decendant applicationn
        os.environ["PYTHONPATH"] = \
            "{};{}".format(os.environ["PYTHONPATH"], frameworkPythonPathFolder)
        # Import the module
        import frameworkPythonPathModule
        msg = frameworkPythonPathModule.returnMsg()
        self.log_debug("%s{}".format(msg) % self)


    def destroy_framework(self):
        self.log_debug("%s: Destroying ExampleFramework..." % self)
