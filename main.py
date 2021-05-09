import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import random
import discord
from discord.ext import tasks
import time
import urllib.request
import json
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

client_id = 'YOUR SPOTIFY CLIENT_ID'
client_secret = 'YOUR SPOTIFY CLIENT_SECRET'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

TOKEN = 'YOUR DISCORD TOKEN'

async def SendMessage():
    url = 'https://sekai-world.github.io/sekai-master-db-diff/musics.json'
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    while True:
        kadai = random.choice(content)
        if int(time.time() * 1000) > kadai['publishedAt']:
            print(kadai['title'])
            break

    channel = client.get_channel(CHANNEL_ID)
    member_mention = "ROLL_ID"
    message = member_mention + ' チャレンジライブやった？\n今日の課題曲は' + kadai['title']

    #spotify
    url = 'https://open.spotify.com/playlist/5ASYsDey4ruxdzZa2U321E?si=c546c825ceca48e5'
    results = spotify.playlist(url)
    for n in range(len((results['tracks']['items']))):
        if kadai['title'] in results['tracks']['items'][n]['track']['name']:
            message += '\n'
            message += results['tracks']['items'][n]['track']['external_urls']['spotify']
    
    await channel.send(message)
    time.sleep(60)

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="プロセカ", type=1))
    timeloop.start()

@tasks.loop(seconds=30)
async def timeloop():
    now = datetime.now(JST).strftime('%H:%M')
    if now == '00:00':
        await SendMessage()

client.run(TOKEN)
