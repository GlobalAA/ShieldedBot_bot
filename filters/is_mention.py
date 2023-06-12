from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsMentionFilter(BoundFilter):
	key = "is_mention"

	def __init__(self, is_mention: bool):
		self.is_mention = is_mention

	async def check(self, message: types.Message):
		mention = lambda entity: entity.type == types.MessageEntityType.TEXT_MENTION or entity.type == types.MessageEntityType.MENTION
		return len([entity for entity in message.entities if mention(entity)]) > 0