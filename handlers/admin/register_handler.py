from aiogram import types

from dispatcher import dp

# Commands
from .commands.ban_command import ban_command
from .commands.mute_command import mute_user
from .commands.unban_command import unban_command
from .commands.unmute_command import unmute_user

dp.register_message_handler(ban_command, commands=["ban"], is_admin=True)
dp.register_message_handler(unban_command, commands=["unban"], chat_type=[types.ChatType.PRIVATE], is_admin=True)
dp.register_message_handler(unmute_user, commands=["unmute"], chat_type=[types.ChatType.PRIVATE], is_admin=True)
dp.register_message_handler(mute_user, commands=["mute"], is_admin=True)
