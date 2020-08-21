# tk-framework-example
 example tk-framework demonstrating how to access via sgtk hooks and applications

Add the framework in \config\env\includes\frameworks.yml
	Example can be found:  \exampleFilesRequiringModification\config\env\includes\frameworks.yml
Then load the framework from the appropriate app or hook
	App Example:  git\tk-substancepainter\v1.2.2\info.yml
		# Note there's something about adding the framework to the app I'm missing
		# I would have expected the app to load the framework which would have made the modules available via SYS.PATH.APPEND() or OS.ENVIRON["PYTHONPATH"]
	Hook Example:  exampleFilesRequiringModification\config\hooks\tk-multi-launchapp\before_app_launch.py
		fw = self.load_framework("tk-framework-example")
		pythonfolderExampleModule = fw.import_module("pythonfolderExampleModule")  
			We can append paths in framework.py called via the "load_framework" command
			We can append paths in framework/python/__init__.py called via the "fw.import_module" command

	I currently feel that adding the relative imports via "load_framework" is the superior option as the paths are inherited by the decendant application and the hook as long as the "load_framework" is called.  
	By appending in the framework/python/__init__.py called via "fw.import_module", if you don't import a module in the hook, the paths aren't available in the application.  