import os
import pkgutil
import importlib
import discord

def set_client(client):
	Command.client = client;

def try_handle(message):
	return Command.try_handle(message)

class Command:

	# Static
	client = None
	implementation = {}
	fn_exec = None

	# Member
	aliases = []

	def __init__(self, fn_exec, aliases=[]):
		if not isinstance(aliases, list):
			aliases = []
		self.fn_exec = fn_exec
		self.aliases = aliases

	def execute(self, message, arg):
		return self.fn_exec(self, message, arg)

	@classmethod
	def register(cls, name, fn_exec, aliases=[]):
		cls.implementation[name] = cls(fn_exec, aliases)

	@classmethod
	def get_implemented_command(cls, command_str):
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

		msg_parts = msg_content.split(' ', 3)
		command_str = len(msg_parts) > 1 and msg_parts[1]
		arg_str = len(msg_parts) > 2 and msg_parts[2] or ''

		cmd = cls.get_implemented_command(command_str)
		if cmd is None:
			await cls.client.send_message(message.channel, '%s Command `%s` is not recognized-chao!' % (message.author.mention, command_str))
			await cls.client.add_reaction(message, '\u26A0')
			return False

		try:
			await cmd.execute(message, arg_str)
		except discord.errors.Forbidden as e:
			await cls.client.send_message(message.channel, "%s I'm not allowed to do that-chao!" % (message.author.mention))
			await cls.client.add_reaction(message, '\u26A0')
		except:
			await cls.client.send_message(message.channel, "%s I couldn't process the request. Something went wrong-chao..." % (message.author.mention))
			await cls.client.add_reaction(message, '\u26A0')
			return False

		return True

	@staticmethod
	def init():
		for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
			importlib.import_module('.' + name, __package__)
			module = globals()[name]
			fn_exec = module.execute
			aliases = getattr(module, 'aliases', None)
			Command.register(name,fn_exec, aliases)

Command.init()