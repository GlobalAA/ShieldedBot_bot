from aiogram import types

from dispatcher import dp

# Commands
from .commands.ban_command import ban_command

dp.register_message_handler(ban_command, commands=["ban"], is_admin=True)
