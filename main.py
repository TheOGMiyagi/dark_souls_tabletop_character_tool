"""<Module "dark_souls_tabletop_character_tool/main.py"
Description:
The Main Module of the project.
"""
#import [Module/Package]
import logging
from logging.handlers import TimedRotatingFileHandler

from src.character import Character

# LOGGER SETUP
logging.basicConfig(filename='scriptlogs.txt', level=logging.WARN)
TRFH = TimedRotatingFileHandler('scriptlogs.txt', when='midnight')

# MAIN METHOD
def main():
	"""<Method "dark_souls_tabletop_character_tool/main.main()">
	Description:
	This method contains the main logic when this module is run directly.
	"""
	_mode = input('What mode do you want to generate this character in?\n\n1. Manual\n2. Random\n\n')
	if not isinstance(_mode, str):
		logging.warn('Invalid type provided for _mode.')
	if _mode[0] == '1' or _mode.lower() == 'manual':
		_test_char = Character(mode='manual')
	elif _mode[0] == '2' or _mode.lower() == 'random':
		_test_char = Character()
	
	print('Generating Dark Souls Character...', _test_char, sep='\n')


# DRIVER CODE
if __name__ == '__main__':
	main()
	
	while True:
		_again = input("\nWould you like to run this program again?\n[Y/N]\n")
		try:
			if _again.lower() == 'y' or _again.lower() == 'yes':
				print('\n')
				main()
			elif _again.lower() == 'n' or _again.lower() == 'no':
				break
			else:
				raise ValueError('Invalid Response To "_again" Prompt.')
		except ValueError as e:
			logging.error(e)
			continue
else:
	print(f'{__name__} has been successfully imported.')
