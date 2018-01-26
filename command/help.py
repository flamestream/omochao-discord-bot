async def execute(self, message, arg):

	await self.client.add_reaction_ack(message)

	out = None

	if arg:
		if arg in self.implementation:
			out = self.implementation[arg].help_message
			if not out:
				out = 'That command has no documentation yet-chao...'
			else:
				out = 'Here is a detailed explanation of `%s`-chao.\n```\n%s\n```' % (arg, out)
		else:
			out = 'Command `%s` does not exist-chao!' % arg

	if not out:
		out = get_default_message(self)

	await self.client.reply(message, out)

def get_default_message(self):

	command_list_str = '\n'.join('- %s' % c for c in self.implementation.keys())
	out = '''I'm here to help-chao!
```diff
Here are the available commands:
%s

To run a command:
    -chao [command] [args...]

For more information about a specific command:
    -chao help [command name]
```''' % (command_list_str)
	return out

help_message = '''Outputs a detailed explanation of a specified command.
If no argument is passed, then a list of command is displayed.'''

aliases = [
	'halp'
]
