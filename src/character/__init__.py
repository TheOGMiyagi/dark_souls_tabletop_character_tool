"""<Module "dark_souls_tabletop_character_tool/src/character/__init__.py"
Description:
This script initializes the /src/character/ package.
"""
import logging

from .base_class import Character
from ..utils.logging_tools import acknowledge_import


if __name__ != '__main__':
	acknowledge_import(output_method=logging.debug, docstring=False)
