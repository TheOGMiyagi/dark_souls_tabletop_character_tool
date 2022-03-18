"""<Module "dark_souls_tabletop_character_tool/src/utils/__init__.py"
Description:
This script initializes the /src/utils/ package.
"""
import logging
from .logging_tools import acknowledge_import

if __name__ != '__main__':
	acknowledge_import(output_method=logging.debug, docstring=False)
