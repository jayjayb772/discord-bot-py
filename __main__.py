import os
import discord
import clientclass as c


client = c.MyClient()
client.run(os.environ.get('DEV_TOKEN'))