from aiogram import types

from dispatcher import bot


async def ban_command(message: types.Message):
	if not message.reply_to_message:
		return await message.reply("Эта команда должна быть ответом на сообщение!")

	reply = message.reply_to_message

	if reply.from_user.id == message.from_user.id:
		return await message.reply("Вы не можете забанить самого себя")

	await bot.ban_chat_member(message.chat.id, reply.from_user.id)
	await bot.send_message(message.chat.id, f"Пользователь {reply.from_user.username or reply.from_user.first_name} был заблокирован администратором!")
	await message.delete()