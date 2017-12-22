import os
import discord
import asyncio
import command

client = discord.Client()
command.set_client(client);

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):

	if not await command.try_handle(message) is None:
		return

	if message.content == "ping?":
		await client.send_message(message.channel, "pong-chao!")

client.run(os.environ['DISCORD_TOKEN'])