from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_btn= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" O'zbek adabiyoti"),
            KeyboardButton(text=' Jahon adabiyoti')
        ],
        [
            KeyboardButton(text='REKLAMA'),
            KeyboardButton(text='English')
        ],

        [
            KeyboardButton(text='kontaktni ulashish',request_contact=True),
            KeyboardButton(text='Lokatsiyani tashlash',request_location=True)
        ],        [
            KeyboardButton(text=' Aloqa')
        ],
    ],
    resize_keyboard=True
)
uzbek_adabiyot=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Abdulla Qodiriy'),

            KeyboardButton(text='Oybek')
        ],
        [
            KeyboardButton(text='Said Ahmad'),
            KeyboardButton(text="O'tkir Hoshimov")
        ],
        [
            KeyboardButton(text="Asosiy Menuga qaytish")
        ]
    ],
    resize_keyboard=True
)

jahon_adabiyot=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Aleksandr Pushkin'),

            KeyboardButton(text='Lev Tolstoy')
        ],
        [
            KeyboardButton(text='Jek London'),
            KeyboardButton(text="Chingiz Aytmatov")
        ],
        [
            KeyboardButton(text="Asosiy Menuga qaytish")
        ]
    ],

    resize_keyboard=True

)