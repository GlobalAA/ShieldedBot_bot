import os

from aiogram import exceptions, types

from dispatcher import bot


async def report_command(message: types.Message):
	if not message.reply_to_message:
		return await message.reply("Эта команда должна быть ответом на сообщение!")
	
	reply = message.reply_to_message

	if reply.from_user.is_bot:
		return await message.reply("Вы не можете отправить жалобу на бота!")

	if reply.from_user.id == message.from_user.id:
		return await message.reply("Вы не можете отправить жалобу на самого себя!")

	if reply.from_user.id == int(os.getenv("OWNER_ID")):
		return await message.reply("Вы не можете отправить жалобу на администратора канала!")

	reply_message_user_id = reply.from_user.id
	message_args = message.get_args()

	if len(message_args.strip()) <= 0:
		return await message.reply("У вашей жалобы должна быть причина!")

	report_message = f""" 
User id: {reply_message_user_id}
Username: {reply.from_user.username or 'отсутствует'}
Firstname: {reply.from_user.first_name or 'отсутствует'}
Lastname: {reply.from_user.last_name or 'отсутствует'}
Reason for the report: {message_args}

From username: {message.from_user.username or 'отсутствует'}
From firstname: {message.from_user.first_name or 'отсутствует'}
From lastname: {message.from_user.last_name or 'отсутствует'}
	"""

	try:
		approval_button = types.InlineKeyboardButton("✅", callback_data=f"report approval {reply_message_user_id} {reply.from_user.username or reply.from_user.first_name}")
		discard_button = types.InlineKeyboardButton("❌", callback_data=f"report discard {reply_message_user_id}")
		keyboard = types.InlineKeyboardMarkup(row_width=2)
		keyboard.row(approval_button, discard_button)
		await bot.send_message(os.getenv("OWNER_ID"), report_message, reply_markup=keyboard)
	except exceptions.ChatNotFound as e:
		print("Chat not found!")
	except exceptions.CantInitiateConversation as e:
		print(e)

	await message.delete()