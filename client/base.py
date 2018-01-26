import command

class Client:

	async def on_message(self, message):
		await command.try_handle(message)

	async def add_reaction_warn(self, message):
		await self.add_reaction(message, '\u26A0')

	async def add_reaction_ack(self, message):
		await self.add_reaction(message, '\u2705')


	async def add_reaction(self, message, reaction):
		raise RuntimeError('Not implemented')

	async def reply(self, original_message, reply_message_text):
		raise RuntimeError('Not implemented')

	async def add_roles(self, user, role):
		raise RuntimeError('Not implemented')

	async def remove_roles(self, user, role):
		raise RuntimeError('Not implemented')