from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import discord
from discord.ext import tasks
import time
import urllib.request
import json
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

TOKEN = os.getenv("DISCORD_TOKEN", "")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

todays_music: str = "error"


def jiho():
    url = 'https://sekai-world.github.io/sekai-master-db-diff/musics.json'
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    while True:
        kadai = random.choice(content)
        if int(time.time() * 1000) > kadai['publishedAt']:
            print(kadai['title'])
            break

    message: str = kadai['title']

    # spotify
    url = 'https://open.spotify.com/playlist/5ASYsDey4ruxdzZa2U321E?si=c546c825ceca48e5'
    results = spotify.playlist(url, market="JP")
    for n in range(len((results['tracks']['items']))):
        if kadai['title'] in results['tracks']['items'][n]['track']['name']:
            message += 'だよ\n'
            message += results['tracks']['items'][n]['track']['external_urls']['spotify']
    global todays_music
    todays_music = message
    return message


client = discord.Client(intents=discord.Intents.default())
os.makedirs("tmp", exist_ok=True)


@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="プロセカ", type=1))
    timeloop.start()


@tasks.loop(seconds=30)
async def timeloop():
    now = datetime.now(JST).strftime('%H:%M')
    if now == '04:10':
        channel = client.get_channel(CHANNEL_ID)
        global todays_music
        todays_music = jiho()
        await channel.send('明日の課題曲は' + todays_music)
        time.sleep(60)

    if now == '00:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<@&764727893271117825>' + ' チャレンジライブやった？\n' + '今日の課題曲は' + todays_music)
        time.sleep(60)

client.run(TOKEN)
