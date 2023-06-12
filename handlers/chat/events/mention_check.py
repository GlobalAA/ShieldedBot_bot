from aiogram import types


async def mention(message: types.Message):
	await message.delete()