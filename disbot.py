#! /usr/bin/python
#NICK PARBS 

import discord
import asyncio
import os
import re
import time
import random
import sys

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
@client.event
async def on_member_join(member):
	msg = member.name + " has joined the channel! Welcome! to " + member.server.name
	await client.send_message(member.server, msg)
	
@client.event
async def on_message(message):
	msgin = message.content.lower
	if message.content.startswith('!dis '):
		print(message.author.name + ' ' + message.content)
		
		with open("diss.txt", "r") as f:
			diss = f.read()
			diss = diss.split("\n")
			diss = list(filter(None, diss))
			
		msg = message.content.replace('!dis ','')
		msg = msg + ' ' + random.choice(diss)
		await client.send_message(message.channel, msg)
	
	elif message.content.startswith('!joke'):
		print(message.author.name + ' ' + message.content)
		
		with open("jokes.txt", "r") as f:
			jokes = f.read()
			jokes = jokes.split("\n\n")
			jokes = list(filter(None, jokes))
			
		joke = random.choice(jokes)
		msg = 'joke ' + str(jokes.index(joke)) + ': ' + joke
		await client.send_message(message.channel, msg)
	
	elif message.content.startswith('!test'):
		print(message.author.name + ' ' + message.content)
		await client.send_message(message.channel, 'test')
		
	elif "fuck you" in message.content and message.author.name != "Dis-Bot":
		print(message.author.name + ' ' + message.content)
		await client.send_message(message.channel, 'no, fuckkkkk you!')
		
	elif message.content.startswith('!sleep '):
		msg = message.content
		mins = float(msg.replace('!sleep ',''))
		if isinstance(mins, float):
			secs = 60 * mins
			print('sleeping ' + str(mins) + ' mins')
			await asyncio.sleep(mins)
			print('done sleeping')
			await client.send_message(message.channel, 'Done sleeping')
			
		else:
			print(secs)
			await client.send_message(message.channel, 'Invalid time')
			
	elif message.content.startswith('!die'):
		sys.exit()
	
try:	
	client.run("INSERT TOKEN HERE")	
except Exception:
	print('fail')
