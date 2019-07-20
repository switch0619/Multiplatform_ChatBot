# encoding: utf-8
import config
import asyncio
import discord
token = config.Discord_bot_token
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(f'{config.set_command}help'):
        await message.channel.send('!help 도움말\n!정보 봇 정보\n!후원\n!나무위키\n!위키피디아\n!네이버\n!구글\n!구글논문\n!디비피아\n!유튜브\n!스택\n!트위치\n!트게더')
    if message.content.startswith(f'{config.set_command}정보'):
        await message.channel.send('https://github.com/EuiseoCha/Multiplatform_ChatBot')
    if message.content.startswith(f'{config.set_command}후원'):
        await message.channel.send('개발자에게 후원하기 :) \nhttps://twip.kr/zeroday0619')
    if message.content.startswith(f'{config.set_command}나무위키'):
        await message.channel.send('https://namu.wiki/w/나무위키:대문')
    if message.content.startswith(f'{config.set_command}위키피디아'):
        await message.channel.send('https://ko.wikipedia.org/wiki/위키백과:대문')
    if message.content.startswith(f'{config.set_command}네이버'):
        await message.channel.send('https://naver.com')
    if message.content.startswith(f'{config.set_command}구글'):
        await message.channel.send('https://google.com')
    if message.content.startswith(f'{config.set_command}구글논문'):
        await message.channel.send('https://scholar.google.co.kr/')
    if message.content.startswith(f'{config.set_command}디비피아'):
        await message.channel.send('https://dbpia.co.kr/')
    if message.content.startswith(f'{config.set_command}유튜브'):
        await message.channel.send('https://youtube.com')
    if message.content.startswith(f'{config.set_command}스택'):
        await message.channel.send('https://stackoverflow.com/')
    if message.content.startswith(f'{config.set_command}트위치'):
        await message.channel.send('https://twitch.tv/')
    if message.content.startswith(f'{config.set_command}트게더'):
        await message.channel.send('https://tgd.kr/')
client.run(token)