import sys
import os
import pkgutil
import importlib
import discord
import traceback
from colorama import Style, Fore

### Module API ###

def set_client(client):
	Command.client = client;

def try_handle(message):
	return Command.try_handle(message)

### END module API ###

class Command:

	# Static
	client = None
	implementation = {}

	# Member
	fn_exec = None
	help_message = None
	aliases = []

	def __init__(self, fn_exec, help_message=None, aliases=[]):
		if not isinstance(aliases, list):
			aliases = []
		self.fn_exec = fn_exec
		self.help_message = help_message
		self.aliases = aliases

	@staticmethod
	def init():
		for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
			importlib.import_module('.' + name, __package__)
			module = globals()[name]
			fn_exec = module.execute
			help_message = getattr(module, 'help_message', None)
			aliases = getattr(module, 'aliases', None)
			Command._register(name, fn_exec, help_message, aliases)

	# Command function runner
	def _execute(self, message, arg):
		return self.fn_exec(self, message, arg)

	# Command string-function pairer
	@classmethod
	def _register(cls, name, fn_exec, help_message, aliases=[]):
		cls.implementation[name] = cls(fn_exec, help_message, aliases)

	# Command look-up by string
	@classmethod
	def _get_implemented_command(cls, command_str):
		for name, cmd in cls.implementation.items():

			if command_str == name:
				return cmd

			for alias in cmd.aliases:
				if command_str == alias:
					return cmd

	@classmethod
	async def try_handle(cls, message):

		msg_content = message.content
		# print('Handling %s...' % message.content)

		if not msg_content.startswith('-chao '):
			return

		msg_parts = msg_content.split(' ', 2)
		command_str = len(msg_parts) > 1 and msg_parts[1]
		arg_str = len(msg_parts) > 2 and msg_parts[2] or ''

		cmd = cls._get_implemented_command(command_str)
		if cmd is None:
			await cls.client.reply(message, 'Command `%s` is not recognized-chao!' % (command_str))
			await cls.client.add_reaction(message, '\u26A0')
			return False

		try:
			await cmd._execute(message, arg_str)
		except discord.errors.Forbidden as e:
			await cls.client.reply(message, "I'm not allowed to do that-chao!")
			await cls.client.add_reaction(message, '\u26A0')
		except:
			# Log error
			print(Fore.RED + Style.BRIGHT, end='')
			print('Error on input: %s' % msg_content)
			traceback.print_exc()
			print(Style.RESET_ALL, end='')
			# Feedback
			await cls.client.reply(message, "I couldn't process the request. Something went wrong-chao...")
			await cls.client.add_reaction(message, '\u26A0')
			return False

		return True

Command.init()