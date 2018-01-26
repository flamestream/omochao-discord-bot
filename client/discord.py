import os
import discord
from client.base import Client as Base

class Client(Base):

	base_client = None
	def __init__(self):

		self.base_client = discord.Client()

		@self.base_client.event
		async def on_ready():
			print('Logged in as')
			print(self.base_client.user.name)
			print(self.base_client.user.id)
			print('------')

		@self.base_client.event
		async def on_message(message):
			await self.on_message(message)

	def run(self):
		self.base_client.run(os.environ['DISCORD_TOKEN'])

	async def add_reaction(self, message, reaction):
		await self.base_client.add_reaction(message, reaction)

	async def reply(self, message, reply_text):
		await self.base_client.send_message(message.channel, "%s %s" % (message.author.mention, reply_text))

	async def add_roles(self, user, role):
		await self.base_client.add_roles(user, role)

	async def remove_roles(self, user, role):
		await self.base_client.remove_roles(user, role)