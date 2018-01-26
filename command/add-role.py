import os

whitelist = ['artist', 'animator', 'writer', 'gamer']

async def execute(self, message, arg):

	user = message.author

	if not arg.lower() in whitelist:
		await self.client.reply(message, 'I can only handle the following roles-chao: %s' % ', '.join('`%s`' % v for v in whitelist))
		await self.client.add_reaction_warn(message)
		return

	target_role = None
	matching_roles = [r for r in message.server.roles if r.name.lower() == arg.lower()]
	if len(matching_roles) >= 1:
		target_role = matching_roles[0]

	if target_role is None:
		await self.client.reply(message, 'I could not find role `%s`-chao...' % arg)
		await self.client.add_reaction_warn(message)
	else:
		await self.client.add_roles(user, target_role)
		await self.client.add_reaction_ack(message)

help_message = '''Grants a role to yourself.
You may have multiple roles assigned to yourself.
Only one role can be granted per command.
I can only grant the following roles: %s

Example usage:
    -chao %s %s''' %  (', '.join(whitelist), os.path.splitext(os.path.basename(__file__))[0], whitelist[0])