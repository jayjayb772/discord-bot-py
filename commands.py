import discord
import os

prefix = "irl!"


def detectPrefix(message):
    return message.content.startswith(prefix)


async def determineCommand(message):
    content = message.content[4:]
    args = content.split()
    cmd = args[0]
    if cmd == 'say':
        await cmdSay(message, args)
    return


async def cmdSay(message, args):
    await message.delete()
    await message.channel.send(' '.join(args[1:]))
    return
