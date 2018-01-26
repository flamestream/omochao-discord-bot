import command
from client.cli import Client

client = Client()
command.set_client(client)
client.run()
