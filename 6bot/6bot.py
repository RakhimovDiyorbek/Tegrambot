from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from default_btn import start_btn,uzbek_adabiyot,jahon_adabiyot

BOT_TOKEN = '7428319829:AAE8Uusx1D3YbrXr_Pyz9CW7BXArK5zajSU'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_fun(msg: Message):
    await msg.answer(f"Assalomu alaykum {msg.from_user.full_name}\n.Kutubxona Borimizga xush kelibsiz!",reply_markup=start_btn)



    @dp.message_handler(text='Aloqa')
    async def aloqa(msg:Message):
        await msg.answer("Savol va takliflaringiz bo'lsa, ushbu https://t.me/RakhimovDiyorbek ga yozib qoldirishingiz mumkin (Biz uni albatta ko'rib chiqamiz)")


    @dp.message_handler(text='English')
    async def ingliz(msg:Message):
        await msg.answer("https://telegra.ph/IELTS-Books-11-04")



    @dp.message_handler(text="O'zbek adabiyoti")
    async def uzb_adabiyoti(msg:Message):
        await msg.answer('Sizga qaysi yozuvchining asarlari kerak? Tanlang! ',reply_markup=uzbek_adabiyot)



    @dp.message_handler(text='Asosiy Menuga qaytish')
    async def orqaga(msg:Message):
        await msg.answer('Asosiy menuga qaytdingiz',reply_markup=start_btn)
        @dp.message_handler(text='REKLAMA')
        async def kanallar_fun(msg:Message):
            await msg.answer()


    @dp.message_handler(text="REKLAMA")
    async def reklama(msg:Message):
        image=open('static/dd.jpg','rb')
        txt='''Raximov
    Diyorbek
    Qayim o'g'li   '''
        await  msg.answer_photo(photo=image,caption=txt)


@dp.message_handler(text='Abdulla Qodiriy')
async def qodiriy(msg:Message):
    kitob=('Kitoblar/Baxtsiz kuyov.pdf','Kitoblar/Abdulla Qodiriy.Diyori bakr.pdf')
    for i in kitob:
        await msg.answer_document(document=open(i,'rb'))



@dp.message_handler(text='Oybek')
async def ffvdsvd(msg: Message):
    kitob1 =open('Kitoblar/Oybek. Bolalik.pdf','rb')
    kitob2=open('Kitoblar/Oybek. Quyosh qoraymas.pdf','rb')
    kitob3 = open('Kitoblar/Oybek. Bola Alisher.pdf', 'rb')
    await msg.answer_document(document=kitob1)
    await msg.answer_document(document=kitob2)
    await msg.answer_document(document=kitob3)


@dp.message_handler(text='Said Ahmad')
async def ahmadd(msg: Message):
    kitob4 =open("Kitoblar/Said Ahmad. Cho'l burguti.pdf",'rb')
    kitob5=open("Kitoblar/Said Ahmad. Sobiq o'g'ri.pdf",'rb')
    kitob6 = open('Kitoblar/UFQ.apk', 'rb')
    await msg.answer_document(document=kitob4)
    await msg.answer_document(document=kitob5)
    await msg.answer_document(document=kitob6)



@dp.message_handler(text="O'tkir Hoshimov")
async def hoshimov(msg: Message):
    kitob1 =open("Kitoblar/O'tkir Hoshimov .Ikki eshik orasi.pdf",'rb')
    kitob2=open("Kitoblar/O'tkir Hoshimov Dunyoning ishlari.pdf",'rb')
    kitob3 = open("Kitoblar/O'tkir Hoshimov. Nur borki, soya bor.pdf", 'rb')
    await msg.answer_document(document=kitob1)
    await msg.answer_document(document=kitob2)
    await msg.answer_document(document=kitob3)


@dp.message_handler(text="Jahon adabiyoti")
async def jhn_adabiyoti(msg:Message):
    await msg.answer('Sizga qaysi yozuvchining asarlari kerak? Tanlang! ',reply_markup=jahon_adabiyot)



@dp.message_handler(text='Lev Tolstoy')
async def fffv(msg: Message):
    kitobj1 =open('Kitoblar/jahon kitoblari/Lev Tolstoy. Urush va tinchlik 1.pdf', 'rb')
    kitobj2=open('Kitoblar/jahon kitoblari/Lev Tolstoy. Urush va tinchlik 2.pdf', 'rb')
    kitobj3 = open('Kitoblar/jahon kitoblari/Lev Tolstoy. Urush va tinchlik 3.pdf', 'rb')
    await msg.answer_document(document=kitobj1)
    await msg.answer_document(document=kitobj2)
    await msg.answer_document(document=kitobj3)


@dp.message_handler(text='Aleksandr Pushkin')
async def fsdfv(msg: Message):
    kitobp1 =open('Kitoblar/jahon kitoblari/Aleksandr Pushkin. Kapitan qizi.pdf', 'rb')
    kitobp2=open('Kitoblar/jahon kitoblari/Aleksandr Pushkin. Suv parisi.pdf', 'rb')
    kitobp3 = open('Kitoblar/jahon kitoblari/Aleksandr Pushkin. Yevgeniy Onegin.pdf', 'rb')
    await msg.answer_document(document=kitobp1)
    await msg.answer_document(document=kitobp2)
    await msg.answer_document(document=kitobp3)

@dp.message_handler(text='Chingiz Aytmatov')
async def fsdfv(msg: Message):
    kitoba1 =open('Kitoblar/jahon kitoblari/Chingiz Aytmatov. Birinchi muallim.pdf', 'rb')
    kitoba2=open('Kitoblar/jahon kitoblari/Chingiz Aytmatov. Erta qaytgan turnalar.pdf', 'rb')
    kitoba3 = open('Kitoblar/jahon kitoblari/Chingiz Aytmatov. Oqkema.pdf', 'rb')
    await msg.answer_document(document=kitoba1)
    await msg.answer_document(document=kitoba2)
    await msg.answer_document(document=kitoba3)

@dp.message_handler(text='Jek London')
async def london(msg: Message):
    kitobl1 =open("Kitoblar/jahon kitoblari/Jek London. Oq so'yloq.pdf", 'rb')
    kitobl2=open('Kitoblar/jahon kitoblari/Hayotga muhabbat (Jek London).pdf', 'rb')
    await msg.answer_document(document=kitobl1)
    await msg.answer_document(document=kitobl2)

# @dp.message_handler(text="kitob")
# async def ki(msg: Message):
#     kitoblar = ['static/kitob.pdf',]
#     for i in kitoblar:
#         await msg.answer_document(document=open(i, 'rb'))

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)








