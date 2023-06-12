import os
from datetime import timedelta

from aiogram.types import Message, chat_permissions


async def mute_user(message: Message):
	if not message.reply_to_message:
		return await message.reply("Ета команда должна быть ответом на сообщение")

	user_id = message.reply_to_message.from_user.id
	seconds = 120

	try:
		if int(message.get_args()):
			seconds = int(message.get_args())
	except:
		return await message.reply("Вы должны указать время")

	await message.bot.restrict_chat_member(
		chat_id=os.getenv("CHAT_ID"), 
		user_id=user_id,                                           
		until_date=timedelta(seconds=seconds),
		permissions=chat_permissions.ChatPermissions(
			can_send_messages=False,
			can_send_polls=False,
			can_send_other_messages=False,
			can_send_media_messages=False
			)
		)
	
	await message.answer("Пользователь успешно был заглушен!")
	await message.delete()
