from aiogram import types


def isLink(message: types.Message):
	entries = [entry for entry in message.entities if entry.type == types.MessageEntityType.URL]
	return True if len(entries) > 0 else False