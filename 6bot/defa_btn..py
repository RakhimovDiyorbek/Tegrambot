from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📞 Aloqa')
        ],
        [
            KeyboardButton(text='✅ FOYDALI KANALLAR VA ULARDA REKLAMA')
        ],
        [
            KeyboardButton(text='🇬🇧 English')
        ],
        [
            KeyboardButton(text="📚 O'zbek adabiyoti"),
            KeyboardButton(text='📚 Jahon adabiyoti')
        ]
    ],
    resize_keyboard=True
)

adabiyot_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 Sbdulla Qodiriy'),
            KeyboardButton(text='👤 Abdulla Fodiriy')
        ],
        [
            KeyboardButton(text='👤 Tbdulla Qodiriy'),
            KeyboardButton(text='👤 Pbdulla Godiriy')
        ],
        [
            KeyboardButton(text='👤 Hbdulla Lodiriy'),
            KeyboardButton(text='👤 Kbdulla Qodiriy')
        ],
        [
            KeyboardButton(text="Asosiy menu")
        ]
    ],
    resize_keyboard=True
)
