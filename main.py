# 1

import base64

password = input("Input: ")
encoded_da = base64.b64encode(password.encode('utf-8'))
decoded_da = base64.b64decode(encoded_da).decode('utf-8')

print("Original password: ", password)
print("Encoded password: ", encoded_da)
print("Decoded password: ", decoded_da)

# 2

import asyncio
import logging
import yaml
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

bot = Bot(token="")
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "<b>Assalomu alaykum!</b> Xush kelibsiz.",
        parse_mode="HTML")
    a = message.from_user.full_name
    b = message.from_user.username
    c = message.from_user.id
    d = {"name": a, "username": b, "id": c}
    with open("file.yaml", 'w') as file_da:
        yaml.dump(d, file_da)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

# 3

import json

with open("file.json", 'w') as data:
    json.dump("Hello World!", data)

# 4

with open("file.yaml", 'w') as file_da:
    file_da.write(input("Ma'lumot kiriting: "))

# 5

import openpyxl

work = openpyxl.Workbook()
sheet = work.active

sheet["A1"] = "Ism"
sheet["A2"] = "Ahmadjon"  # noqa
sheet["A3"] = "Abdulmajid"  # noqa
sheet["A4"] = "Abubakir"  # noqa
sheet["A5"] = "Diyor"  # noqa

sheet["B1"] = "Yosh"
sheet["B2"] = 16
sheet["B3"] = 16
sheet["B4"] = 16
sheet["B5"] = 16

sheet["C1"] = "Turar joy"
sheet["C2"] = "Uzb, Tash"  # noqa
sheet["C3"] = "Uzb, Tash"  # noqa
sheet["C4"] = "Uzb, Tash"  # noqa
sheet["C5"] = "Uzb, Tash"  # noqa

work.save('exel.xlsx')
