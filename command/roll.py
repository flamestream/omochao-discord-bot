import os
import re
import random

async def execute(self, message, arg):

	user = message.author

	minimum = 1
	maximum = 100

	error = None
	if arg:
		matchObj = re.match( r'((\d+)(-|\s))?(\d+)', arg, re.M)
		if matchObj:
			if matchObj.group(4):
				maximum = int(matchObj.group(4))
			if matchObj.group(2):
				minimum = int(matchObj.group(2))
			if maximum < minimum:
				error = True
		else:
			error = True

	if error:
		await self.client.reply(message, 'Argument `%s` is not valid-chao...' % arg)
		await self.client.add_reaction_warn(message)
	else:
		roll = random.randint(minimum, maximum)
		await self.client.reply(message, 'rolled {0} ({1}-{2})'.format(roll, minimum, maximum))
		await self.client.add_reaction_ack(message)

help_message = '''Rolls a dice. The default is 1-100.

Example usage:
    -chao {0}
    -chao {0} 6
    -chao {0} 10-20'''.format(os.path.splitext(os.path.basename(__file__))[0])
