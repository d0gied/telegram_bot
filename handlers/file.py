from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command

from utils.answer_counter import Counter
from utils.manacher import manacher
import os

router = Router()


@router.message(F.document)
async def msg(message: Message, bot: Bot):

    await bot.download(message.document, 'file.txt')
    data = open('file.txt').read()
    res = len(manacher(data))
    Counter.file.append(res)
    print(f"file={res}")
