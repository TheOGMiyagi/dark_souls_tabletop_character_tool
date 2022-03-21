"""<Module "dark_souls_tabletop_character_tool/src/character/base_class.py"
Description:
The Main Module of the project.
"""
#import [Module/Package]
import logging
from logging.handlers import TimedRotatingFileHandler
from random import randint as roll

from ..utils import acknowledge_import


# LOGGER SETUP
logging.basicConfig(filename='scriptlogs.txt', level=logging.WARN)
TRFH = TimedRotatingFileHandler('scriptlogs.txt', when='midnight')

# MODULE METHODS
class Character:
	"""<Class "dark_souls_tabletop_character_tool/src/character/base_class/Character(object)"
	"""
	def __init__(self, **kwargs):
		"""<Method "dark_souls_tabletop_character_tool/src/character/base_class.Character(object).__init__()">
		Description:
		Creates an instance of the Character() class.
		"""
		#mode = kwargs.get('mode', 'random')
		mode = kwargs.get('mode', 'random')
		if not isinstance(mode, str):
			return
		#
		logging.info('A new instance of <Class "main.Character(object)"> is being created!')
		
		#
		def _request_input(stat: str):
			_output = input(f'Please enter your {stat} score.\n(In numeric form)\n')
			return _output
		if mode.lower() == 'manual':
			self.attunement = _request_input('Attunement')
			logging.debug('Attunement Determined By The User...')
			self.dexterity = _request_input('Dexterity')
			logging.debug('Dexterity Determined By The User...')
			self.endurance= _request_input('Endurance')
			logging.debug('Endurance Determined By The User...')
			self.faith = _request_input('Faith')
			logging.debug('Faith Determined By The User...')
			self.intelligence = _request_input('Intelligence')
			logging.debug('Intelligence Determined By The User...')
			self.strength = _request_input('Strength')
			logging.debug('Strength Determined By The User...')
			self.vitality = _request_input('Vitality')
			logging.debug('Vitality Determined By The User...')
		#
		def _stat_roll():
			return roll(1, 6) + roll(1, 6) + 12
		if mode.lower() == 'random':
			self.attunement = _stat_roll()
			logging.debug('Attunement Determined Randomly...')
			self.dexterity = _stat_roll()
			logging.debug('Dexterity Determined Randomly...')
			self.endurance= _stat_roll()
			logging.debug('Endurance Determined Randomly...')
			self.faith = _stat_roll()
			logging.debug('Faith Determined Randomly...')
			self.intelligence = _stat_roll()
			logging.debug('Intelligence Determined Randomly...')
			self.strength = _stat_roll()
			logging.debug('Strength Determined Randomly...')
			self.vitality = _stat_roll()
			logging.debug('Vitality Determined Randomly...')
		#? Regardless of the provided mode of initialization, the logger will confirm it was succeasful.
		logging.debug('Instance initialization completed successfully.')
		self._estus_uses = 5

	def __str__(self):
		"""<Method "dark_souls_tabletop_character_tool/src/character/base_class.Character(object).__str__()">
		Description:
		This method handles the printability of the class and its attributes.
		"""
		logging.info('<Class "main.Character(object)"> is being printed as a string...')
		_stats = (f'Attunememt:\t{self.attunement}\t(AB +{self.attunement_bonus})',
			f'Dexterity:\t{self.dexterity}\t(DB +{self.dexterity_bonus})',
			f'Endurance:\t{self.endurance}\t(EB +{self.endurance_bonus})',
			f'Faith:\t\t{self.faith}\t(FB +{self.faith_bonus})',
			f'Intelligence:\t{self.intelligence}\t(IB +{self.intelligence_bonus})',
			f'Strength:\t{self.strength}\t(SB +{self.strength_bonus})',
			f'Vitality:\t{self.vitality}\t(VB +{self.vitality_bonus})\n',
			f'Level: {self.level}')
		_output = '\n'.join(_stats)
		logging.debug('main.character(object).__str__() completed successfully.')
		return _output
	
	#* ATTUNEMENT
	@property
	def attunement_bonus(self):
		_stat = str(self.attunement)
		return int(_stat[0])
	#* DEXTERITY
	@property
	def dexterity_bonus(self):
		_stat = str(self.dexterity)
		return int(_stat[0])
	#* ENDURANCE
	@property
	def endurance_bonus(self):
		_stat = str(self.endurance)
		return int(_stat[0])
	#* FAITH
	@property
	def faith_bonus(self):
		_stat = str(self.faith)
		return int(_stat[0])
	#* INTELLIGENCE
	@property
	def intelligence_bonus(self):
		_stat = str(self.intelligence)
		return int(_stat[0])
	#* STRENGTH
	@property
	def strength_bonus(self):
		_stat = str(self.strength)
		return int(_stat[0])
	#* VITALITY
	@property
	def vitality_bonus(self):
		_stat = str(self.vitality)
		return int(_stat[0])
	#* LEVEL
	@property
	def level(self):
		"""<Property "dark_souls_tabletop_character_tool/src/character/base_class.Character(object).level">
		Description:
		This method is decorated with the @property decorator, and its purpose is to calculate the character's level.
		"""
		_values = (self.attunement_bonus,
			self.dexterity_bonus,
			self.endurance_bonus,
			self.faith_bonus,
			self.intelligence_bonus,
			self.strength_bonus,
			self.vitality_bonus)
		_level = 0
		for _ in _values:
			_level = _level + _
		return _level
	#* ESTUS USES
	@property
	def estus(self):
		return self._estus_uses
	@estus.setter
	def estus(self, num):
		if num > 5:
			_estus_uses = 5
		elif num <= 0:
			_estus_uses = 0
		else:
			_estus_uses = num
	@estus.deleter
	def estus(self):
		_estus_uses = 0


def main():
	"""<Method "dark_souls_tabletop_character_tool/src/character/base_class.main()">
	Description:
	This method contains the main logic when this module is run directly.
	"""
	def _generate_character():
		_test_char = Character()
		print('Generating Dark Souls Character...\n')
		print(_test_char)
	#? _generate_character is wrapped in a loop to allow for code re-execution.
	_generate_character()
	while True:
		_again = input("\nWould you like to run this program again?\n[Y/N]\n")
		try:
			if _again.lower() == 'y' or _again.lower() == 'yes':
				print('\n')
				_generate_character()
			elif _again.lower() == 'n' or _again.lower() == 'no':
				break
			else:
				raise ValueError('Invalid Response To "_again" Prompt.')
		except ValueError as error:
			logging.error(error)
		continue


# DRIVER CODE
if __name__ == '__main__':
	main()
else:
	acknowledge_import()
