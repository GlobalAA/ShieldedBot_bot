import os

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsAdminFilter(BoundFilter):
	key = "is_admin"

	def __init__(self, is_admin: bool):
		self.is_admin = is_admin

	async def check(self, message: types.Message):
		return message.from_user.id == int(os.getenv("OWNER_ID"))