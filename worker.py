import command
from client.discord import Client

client = Client()
command.set_client(client)
client.run()