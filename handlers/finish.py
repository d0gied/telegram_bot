from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from utils.answer_counter import Counter

router = Router()


@router.message(Command(commands=['finish']))
async def msg(message: Message):
    file = 0
    audio = 0
    if Counter.file:
        file = sum(Counter.file) / len(Counter.file)
    if Counter.audio:
        audio = sum(Counter.audio) / len(Counter.audio)
    
    answer = f'{Counter.text} {file} {Counter.photo} {audio}'
    
    Counter.audio = []
    Counter.text = 0
    Counter.photo = 1
    Counter.file = []
    
    await message.answer(answer)

