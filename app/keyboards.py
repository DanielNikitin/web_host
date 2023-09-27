from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='EUR TO USD'),
     KeyboardButton(text='USD TO EUR')],
    [KeyboardButton(text='Другой Вариант'),
     KeyboardButton(text='Доступные валюты')]
          ]


main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='daily customs garage © 2023')