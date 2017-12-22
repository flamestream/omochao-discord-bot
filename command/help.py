aliases = [
	'halp'
]

async def execute(self, message, arg):

	await self.client.add_reaction(message, '\u2705')
	out = "%s I'm here to help-chao! Here are the available commands: %s" % (message.author.mention, ', '.join(self.implementation.keys()))
	await self.client.send_message(message.channel, out)