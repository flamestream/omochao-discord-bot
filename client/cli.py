import asyncio
from colorama import Style, Fore
from client.base import Client as Base

class Client(Base):

	def run(self):
		loop = asyncio.get_event_loop()
		loop.run_until_complete(self.run_async())
		loop.close()

	async def run_async(self):
		while True:
			in_str = input("> ")
			message = Message(in_str)
			await self.on_message(message)

	async def add_reaction(self, message, reaction):
		print(Fore.BLUE, end='')
		print("Omochao reacted with %s on message:\n    %s" % (reaction, message.content))
		print(Style.RESET_ALL, end='')

	async def reply(self, original_message, reply_message_text):
		print(Fore.GREEN, end='')
		print("Omochao: @you %s" % (reply_message_text))
		print(Style.RESET_ALL, end='')

	async def add_roles(self, user, role):
		print(Fore.BLUE, end='')
		print("Role `%s` given to `%s`" % (role.name, user))
		print(Style.RESET_ALL, end='')

	async def remove_roles(self, user, role):
		print(Fore.BLUE, end='')
		print("Role `%s` revoked from `%s`" % (role.name, user))
		print(Style.RESET_ALL, end='')

### MOCK TEST RELATED ###

class Role:
	name = ''
	def __init__(self, name):
		self.name = name
test_server_roles = [Role('artist'), Role('animator'), Role('writer'), Role('gamer')]
test_user_roles = []

class Server:
	roles = test_server_roles
test_server = Server()

class Message:
	author = 'me'
	content = None
	server = test_server
	def __init__(self, content):
		self.content = content
