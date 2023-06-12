from aiogram import types


async def on_user_event(message: types.Message):
	await message.delete()