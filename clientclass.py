import discord
import os
import commands as cmd


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(activity=discord.Game("with the API"))

    async def on_message(self, message):
        if(cmd.detectPrefix(message)):
            #Starts with prefix
            print('Contains prefix!')
            await cmd.determineCommand(message)





            return
        else:
            print('Message from {0.author}: {0.content}'.format(message))

