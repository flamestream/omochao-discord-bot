import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content == "ping":
        await client.send_message(message.channel, "pong-chao!")

client.run('epB55MRnsxcUTD2kVwiNROC7zZUKZsp5')