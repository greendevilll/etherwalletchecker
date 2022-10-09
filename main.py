import openpyxl
from configparser import ConfigParser as cfgparserwhat
import requests
import api
from os import system as cmd
import json
import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import platform



etherapi = api.EtherAPI()


config = cfgparserwhat()
config.read("cfg.ini")



API_TOKEN = config['BOT_SETTINGS']['token']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def main():

    @dp.message_handler()
    async def test(message: types.Message,callback_query:types.CallbackQuery=None):
        eth_balance = await etherapi.get_balance(message.text)
        eth_usd_course = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD").json()['USD']
        usd_balance = eth_balance*eth_usd_course
        await message.reply(f"eth: {eth_balance}\nusd:{usd_balance}")

if __name__ == "__main__":
    main()
    executor.start_polling(dp, skip_updates=True)

