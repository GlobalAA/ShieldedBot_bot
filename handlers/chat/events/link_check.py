from aiogram import types
from urlextract import URLExtract

from dispatcher import bot
from utils.isLink import isLink


async def bad_link(message: types.Message):
	extractor = URLExtract()
	name = first if (first := message.from_user.first_name) else message.from_user.last_name
	if extractor.find_urls(name):
		await message.delete()
		await bot.kick_chat_member(message.chat.id, message.from_user.id)

	if isLink(message):
		await message.delete()