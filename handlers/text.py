from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command

import re

from utils.answer_counter import Counter

router = Router()


@router.message(F.text)
async def msg(message: Message):
    clean = re.sub('[^A-Za-zА-Яа-я ]', '', message.text.lower())
    for word in clean.split():
        if word == word[::-1]:
            Counter.text += 1
    print(f"text={Counter.text}")
