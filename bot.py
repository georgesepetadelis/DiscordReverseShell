import discord
import os

client = discord.Client()
token = "YOUR_TOKEN_ID" 

async def send_custom_msg(msg):
	await message.channel.send(msg)

@client.event
async def on_ready():
  print("logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("shutdown"):
    # Shutdown the System
    await message.channel.send("okay, i will shutdown your PC")
    os.system("shutdown -p")
    
  if message.content.startswith("restart"):
    # Restart the System
    os.system("shutdown -r")
    await message.channel.send("okay, i will restart your PC in 1 minute")

  if message.content.startswith("c restart"):
    # Restart the System
    os.system("shutdown -a")
    await message.channel.send("okay, i aborted the restart")

  else:
    # excecute message as system command  
    print("command completed successfully")
    os.system(message.content)

client.run(token)
