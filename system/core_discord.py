# encoding: utf-8
from config import Discord_bot_token as Discord_bot_token
from config import set_command as set_command
from config import DEBUG as DEBUG 
from config import NAME as NAME
import discord

app = discord.client() 
token = Discord_bot_token

@app.event 
async def ready(): 
    print('다음으로 로그인합니다: ') 
    print(app.user.name) 
    print(app.user.id)
    print('_____________________')
    await app.change_presence(game=discord.game(name=f'새로운 시작 :) {NAME} 입니다.', type=1))

@app.event
async def on_message(message):
  if message.author.bot:
    return None
  if message.content == f'{set_command}help':
    await app.send_message(message.channel, '')
  
app.run(token) 

