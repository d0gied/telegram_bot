from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
import re
import pymorphy2


from utils.answer_counter import Counter

router = Router()

morph = pymorphy2.MorphAnalyzer(lang='ru')

@router.message(F.photo)
async def msg(message: Message):
    text = message.caption
    if not text:
        Counter.photo = 0
        return
    clean = re.sub('[^A-Za-zА-Яа-я ]', '', text.lower())
    ans = 0
    for word in clean.split():
        if morph.parse(word)[0].tag.POS in ("ADJF", "PRTF", "ADJS"):
            ans += 1
    Counter.photo *= ans
    print(f'photo={ans}')

