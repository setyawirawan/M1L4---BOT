def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result


def secret_function (a, b):
    # Tulis kode Kamu di sini!
    gabung = str(a) + str(b) 
    return gabung


print(double_letter("Hello"))
print(secret_function(1, 2))
print(secret_function("Hello, ", "world!"))

alghifari  to  Everyone 11:20 AM
gmna tdi kak:)

Dzulfaq Ibnu Najib  to  Everyone 11:25 AM
import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
import discord
# import * - adalah cara cepat untuk mengimpor semua file di perpustakaan
from bot_logic import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan memindahkan hak istimewa
client = discord.Client(intents=intents)


# Setelah bot siap, ia akan mencetak namanya!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Saya! Saya bot!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Tidak dapat memproses perintah ini, maaf")

client.run(settings["TOeKEN"])
