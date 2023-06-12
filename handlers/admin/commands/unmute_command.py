import os
from datetime import timedelta

from aiogram.types import ChatType, Message, chat_permissions

from dispatcher import bot


async def unmute_user(message: Message):
	try:
		await bot.restrict_chat_member(
			chat_id=os.getenv("CHAT_ID"), 
			user_id=message.get_args(),                                           
			permissions=chat_permissions.ChatPermissions(
				can_send_messages=True,
				can_send_polls=True,
				can_send_other_messages=True,
				can_send_media_messages=True
			)
		)
		return await message.answer("Пользователю успешно было выдано право писать!")
	except:
		return await message.reply("Укажите id пользователя")
