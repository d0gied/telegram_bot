from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from utils.answer_counter import Counter

router = Router()


@router.message(F.audio)
async def msg(message: Message):
    text = message.caption
    if not text:
        Counter.audio.append(0)
        return
    ans = text.lower().count('сириус')
    Counter.audio.append(ans)
    print(f'audio={ans}')

