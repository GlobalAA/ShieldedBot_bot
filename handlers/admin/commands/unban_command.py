import os

from aiogram import types

from dispatcher import bot


async def unban_command(message: types.Message):
	try:
		await bot.unban_chat_member(os.getenv("CHAT_ID"), message.get_args(), True)
		return await message.answer("Пользователь успешно разблокирован!")
	except:
		return await message.reply("Укажите id пользователя")