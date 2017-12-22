async def execute(self, message, arg):

	whitelist = ['artist', 'animator', 'writer', 'gamer']
	user = message.author
	out = '%s ' % user.mention

	if not arg.lower() in whitelist:
		self.client.add_reaction(message, '\u26A0')
		await self.client.send_message(message.channel, out + "I can only handle the following roles-chao: %s" % ', '.join('`%s`' % v for v in whitelist))
		await self.client.add_reaction(message, '\u26A0')
		return

	target_role = next(r for r in message.server.roles if r.name.lower() == arg.lower())
	if target_role is None:
		await self.client.send_message(message.channel, out)
		out += 'I could not find role `%s`-chao...' % arg
		await self.client.add_reaction(message, '\u26A0')
	else:
		await self.client.add_roles(user, target_role)
		await self.client.add_reaction(message, '\u2705')
		return

	await self.client.send_message(message.channel, out)