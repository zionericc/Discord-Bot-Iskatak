import discord
import random

hatdog = ['ha', 'Ha', 'HA']

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #replace XXXXXXXXXXXX with your discord app token here

client = discord.Client()

@client.event
async def on_message(message):
    # bot will not reply to itself
    if message.author == client.user:
        return

    # if someone types the same string. ! or any indicator is needed since startswith() is used to make sure no random messages would trigger this accidentally.
    if message.content.startswith('!hello'):
        msg = 'Hi {0.author.mention}'.format(message)   #{0.author.mention} mentions the author of the message
        await client.send_message(message.channel, msg)

    # if only a specific set of string/strings are desired to trigger a message.
    if message.content in hatdog:
        msg = 'Hatdog'.format(message)
        await client.send_message(message.channel, msg)

    # for sending random messages
    if message.content.startswith('!iskatak'):
        msg_r = ['{0.author.mention} I S K A T A K ! ! !'.format(message),
        '{0.author.mention} I S K A T A K ! ? !'.format(message),
        '{0.author.mention} I S K A T A K ? ? ?'.format(message),
        '{0.author.mention} I S K A T A K ? ! ?'.format(message),
        '{0.author.mention} iskatak'.format(message),
        '{0.author.mention} Iskatak'.format(message),
        '{0.author.mention} iSkAtAk'.format(message)]
        await client.send_message(message.channel, random.choice(msg_r))

    # "" or '' can be used depending on your preference.
    if message.content.startswith('!randomstrings'):
        msg_r = ['1st message'.format(message),
        '2nd message'.format(message),
        "3rd message".format(message)]
        await client.send_message(message.channel, random.choice(msg_r))

    if message.content.startswith('!help'):
        msg = '!hello to say Hi.\n\n!iskatak for ISKATAK!!!\n\n!hoyohoy for random quotes or strings'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    hard_coded_channel = discord.Object(id="XXXXXXXXXXXXXX") # replace XXXXXXXXXX with your discord channel here
    await client.send_message(hard_coded_channel, 'ISKATAK IS NOW ONLINE\n\nType !help for a list of commands.')

client.run(TOKEN)