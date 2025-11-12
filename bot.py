import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = 'REMOVED_TOKEN'
CHANNEL_ID = -1002922110765

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

SIGNATURE = ( "<blockquote>🤖 <a href='https://t.me/Mechanicus_True'>Механикус Титаникус</a> 📟</blockquote>\n"
              "<blockquote>✉️ <a href='https://t.me/Uncle_GSS'>Сеть наших каналов</a> ✉️</blockquote>\n\n"
              "#Mechanicus #Adeptus_Mechanicus #AdeptusMechanicus #wh40k #warhammer40k #warhammer" )

@dp.channel_post()
async def add_signature(message: types.Message):
    if message.chat.id != CHANNEL_ID:
        return

    try:
        await message.delete()
    except:
        pass

    caption = SIGNATURE
    if message.caption:
        caption = message.caption + "\n\n" + SIGNATURE
    elif message.text:
        caption = message.text + "\n\n" + SIGNATURE

    try:
        if message.photo:
            await bot.send_photo(CHANNEL_ID, message.photo[-1].file_id, caption=caption)
        elif message.video:
            await bot.send_video(CHANNEL_ID, message.video.file_id, caption=caption)
        elif message.document:
            await bot.send_document(CHANNEL_ID, message.document.file_id, caption=caption)
        elif message.animation:
            await bot.send_animation(CHANNEL_ID, message.animation.file_id, caption=caption)
        elif message.text:
            await bot.send_message(CHANNEL_ID, text=caption)
        else:
            await message.copy_to(CHANNEL_ID, caption=caption)
    except Exception as e:
        print(f"Ошибка: {e}")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
