# bot.py
import os, discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == token:
			break

	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})\n'
	)

	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')
	
@client.event
async def on_message(message):
	if message.author == client.user or message.channel.id == 623968337990254607:
		return
	
	mes = message.content
	
	if mes.startswith('!'):
		command = mes[1:]
		print(command)
	
		response = ''
		
		if command.startswith('letterbomb'):
			response = "For letterbomb, you will need:\n\n- A Wii\n- An SD card (size can be anything, if you need to go buy one 1GB is perfectly fine)\n- Some way for you to read/write data on the SD card (either with a USB adapter or an SD card port on the computer you're using itself\n- A working Wii Remote\n\nIf you plan on using this tutorial to make your Wii play games again, you're also going to need a USB drive containing at the _very_ least 4GB, though something like 16 or even 32GB is closer to what we want.\n\nOnce you have everything, go to https://wii.guide/letterbomb.html. Plailect's guides are great, but sometimes he won't say things that are obvious to him but might not be obvious to others, so if you have any questions, feel free to post them here in #support and LittleCube will answer them."
		if (response != ''):
			print(message.author.name + "#" + message.author.discriminator)
			await message.channel.send(response)

client.run(token)