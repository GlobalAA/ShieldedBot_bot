import os

from aiogram import types

from dispatcher import bot


async def report_callback(callback_query: types.CallbackQuery):
	data = callback_query.data.split(" ")
	callback_type = data[1]

	if callback_type == "discard":
		return	await callback_query.message.delete()
	
	user_id = int(data[-2])

	await bot.kick_chat_member(int(os.getenv("CHAT_ID")), user_id)
	await callback_query.message.delete()
	await bot.send_message(int(os.getenv("CHAT_ID")), f"{data[-1]} был исключен администратором\nПричина: жалоба")