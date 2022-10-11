from dotenv import load_dotenv
from cgitb import text
import os
import requests
import asyncio
import telegram

load_dotenv()

actual_ip = requests.get('https://api.ipify.org/').text

with open("ip.txt", "r") as file:
    previous_ip = file.read()

async def main(text):
    bot = telegram.Bot(os.environ.get('TELEGRAM_TOKEN'))
    bot.send_message(text=text, chat_id=os.environ.get('CHAT_ID'))


if (actual_ip != previous_ip):
    text = f'Mudança no IP! \nIP antigo: {previous_ip} \nIP atual: {actual_ip}'

    if __name__ == '__main__':
        asyncio.run(main(text))

    with open("ip.txt", "w") as file:
        file.write(actual_ip)




