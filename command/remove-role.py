import os
import importlib

add_role_module = importlib.import_module('.add-role', __package__)
whitelist = add_role_module.whitelist

async def execute(self, message, arg):

	user = message.author

	target_role = None
	matching_roles = [r for r in message.server.roles if r.name.lower() == arg.lower()]
	if len(matching_roles) >= 1:
		target_role = matching_roles[0]

	if target_role is None:
		await self.client.reply(message, 'I could not find role `%s`-chao...' % arg)
		await self.client.add_reaction_warn(message)
	else:
		await self.client.remove_roles(user, target_role)
		await self.client.add_reaction_ack(message)

help_message = '''Discards a role from yourself.
You may have multiple roles assigned to yourself.
Only one role can be discarded per command.

Example usage:
    -chao %s %s''' %  (os.path.splitext(os.path.basename(__file__))[0], add_role_module.whitelist[0])