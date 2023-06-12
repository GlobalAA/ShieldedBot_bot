import typing
import warnings
from typing import Union

from aiogram.dispatcher.filters.filters import BoundFilter
from aiogram.types import CallbackQuery, ChatType, Message


class ChatTypeFilter(BoundFilter):
	key = 'chat_type'

	def __init__(self, chat_type: typing.Container[ChatType]):
		if isinstance(chat_type, str):
			chat_type = {chat_type}

		self.chat_type: typing.Set[str] = set(chat_type)

	async def check(self, obj: Union[Message, CallbackQuery]):
		if isinstance(obj, Message):
			obj = obj.chat
		elif isinstance(obj, CallbackQuery):
			obj = obj.message.chat
		else:
			warnings.warn("ChatTypeFilter doesn't support %s as input", type(obj))
			return False

		return obj.type in self.chat_type