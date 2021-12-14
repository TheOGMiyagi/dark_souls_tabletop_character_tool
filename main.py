"""<Module "dark_souls_tabletop_character_tool/main.py"

Description:

The Main Module of the project.

"""

#import [Module/Package]

import logging

from random import randint as roll

# MODULE METHODS

class Character:

	"""<Class "dark_souls_tabletop_character_tool/main/Character(object)"	"""

	def __init__(self):

		"""<Method "dark_souls_tabletop_character_tool/main.Character(object).__init__()">

		Description:

		Creates an instance of the Character() class.

		"""

		self.attunement = roll(1, 6) + 12

		self.dexterity = roll(1, 6) + 12

		self.endurance= roll(1, 6) + 12

		self.faith = roll(1, 6) + 12

		self.intelligence = roll(1, 6) + 12

		self.strength = roll(1, 6) + 12

		self.vitality = roll(1, 6) + 12

	def __str__(self):

		"""<Method "dark_souls_tabletop_character_tool/main.Character(object).__str__()">

		Description:

		This method handles the printability of the class and its attributes.

		"""

		_stats = (f'Attunememt: {self.attunement}',

			f'Dexterity: {self.dexterity}',

			f'Endurance: {self.endurance}',

			f'Faith: {self.faith}',

			f'Intelligence: {self.intelligence}',

			f'Strength: {self.strength}',

			f'Vitality: {self.vitality}')

		_output = '\n'.join(_stats)

		return _output

def main():

	"""<Method "dark_souls_tabletop_character_tool/main.main()">

	Description:

	This method contains the main logic when this module is run directly.

	"""

	_test_char = Character()

	print(_test_char)

# DRIVER CODE

if __name__ == '__main__':

	main()

else:

	print(f'{__name__} has been successfully imported.')
