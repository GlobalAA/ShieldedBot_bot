from aiogram import types
from better_profanity import profanity


async def message_bad_words_detect(message: types.Message):
	profanity.load_censor_words_from_file("wordlist.txt")
	if profanity.contains_profanity(message.text):
		await message.delete()