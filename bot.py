import discord
import os
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.author.send(f'{message.author.name} as regras são:{os.linesep}'
                                       f'1 - Não desrespeitar os membros{os.linesep}'
                                       f'2 - Não falar palavras de baixo calão')

        elif message.content == '?sorte':
            list = [1, 2, 3, 4, 5]
            ref = random.choice(list)
            choice = random.choice(list)
            if choice == ref:
                await message.channel.send(f'{message.author.name} tem muita sorte!')
            else:
                await message.channel.send(f'{message.author.name} está sem sorte!')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f'{member.mention} acabou de entrar no {guild.name}!'
            await guild.system_channel.send(message)

client = MyClient(intents=intents)
client.run('API_KEY')