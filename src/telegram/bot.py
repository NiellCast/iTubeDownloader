from telebot import TeleBot
from dotenv import load_dotenv
from os import getenv


class Bot(TeleBot):
    load_dotenv()

    def __init__(self) -> None:
        super().__init__(token=getenv('TOKEN'), parse_mode=None)
