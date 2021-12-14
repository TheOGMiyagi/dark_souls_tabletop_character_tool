"""<Module "dark_souls_tabletop_character_tool/main.py"
Description:
The Main Module of the project.
"""
#import [Module/Package]
import logging
from random import randint as roll

# LOGGER SETUP
logging.basicConfig(filename='scriptlogs.txt', level=logging.WARN)

# MODULE METHODS
class Character:
	"""<Class "dark_souls_tabletop_character_tool/main/Character(object)"
	"""
	def __init__(self):
		"""<Method "dark_souls_tabletop_character_tool/main.Character(object).__init__()">
		Description:
		Creates an instance of the Character() class.
		"""
		#? This internal function exists solely to add to the readability of __init__()
		logging.info('A new instance of <Class "main.Character(object)"> is being created!')
		def _stat_roll():
			return roll(1, 6) + roll(1, 6) + 12
		self.attunement = _stat_roll()
		logging.debug('Attunement Determined...')
		self.dexterity = _stat_roll()
		logging.debug('Dexterity Determined...')
		self.endurance= _stat_roll()
		logging.debug('Endurance Determined...')
		self.faith = _stat_roll()
		logging.debug('Faith Determined...')
		self.intelligence = _stat_roll()
		logging.debug('Intelligence Determined...')
		self.strength = _stat_roll()
		logging.debug('Strength Determined...')
		self.vitality = _stat_roll()
		logging.debug('Vitality Determined...')
		logging.debug('Instance initialization completed successfully.')
	def __str__(self):
		"""<Method "dark_souls_tabletop_character_tool/main.Character(object).__str__()">
		Description:
		This method handles the printability of the class and its attributes.
		"""
		logging.info('<Class "main.Character(object)"> is being printed as a string...')
		_stats = (f'Attunememt: {self.attunement} (AB +{str(self.attunement)[0]})',
			f'Dexterity: {self.dexterity} (DB +{str(self.dexterity)[0]})',
			f'Endurance: {self.endurance} (EB +{str(self.endurance)[0]})',
			f'Faith: {self.faith} (FB +{str(self.faith)[0]})',
			f'Intelligence: {self.intelligence} (IB +{str(self.intelligence)[0]})',
			f'Strength: {self.strength} (SB +{str(self.strength)[0]})',
			f'Vitality: {self.vitality} (VB +{str(self.vitality)[0]})')
		_output = '\n'.join(_stats)
		logging.debug('main.character(object).__str__() completed successfully.')
		return _output

def main():
	"""<Method "dark_souls_tabletop_character_tool/main.main()">
	Description:
	This method contains the main logic when this module is run directly.
	"""
	_test_char = Character()
	print('Generating Dark Souls Character...\n')
	print(_test_char)

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
