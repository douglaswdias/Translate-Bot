import discord
from langdetect import detect
from libretranslatepy import LibreTranslateAPI
from decouple import config
import os

translate_api = LibreTranslateAPI("https://translate.argosopentech.com/")

supported_languages = [
  "af", "ar", "bg", "bn", "ca", "cs", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "gu", "he","hi", "hr", "hu", "id", "it", "ja", "kn", "ko", "lt", "lv", "mk", "ml", "mr", "ne", "nl", "no", "pa", "pl","pt", "ro", "ru", "sk", "sl", "so", "sq", "sv", "sw", "ta", "te", "th", "tl", "tr", "uk", "ur", "vi"
]

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("Online")


@client.event
async def on_message(message):
  user_message = str(message.content)

  if message.author == client.user:
    return

  message_language = str(detect(user_message))  
  
  try:
    if message_language in supported_languages:
      translation = translate_api.translate(user_message, message_language, "pt")
      await message.channel.send(
        f"🇧🇷 __***Tradução***__ 🇧🇷: {os.linesep}{translation}",
        reference=message)
  except:
    return

TOKEN = config("SECRET")
client.run(TOKEN)
