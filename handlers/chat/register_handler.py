from aiogram import types

from dispatcher import dp

# Callbacks
from .callbacks.report_callback import report_callback
# Commands
from .commands.report_command import report_command
from .events.bad_words_detection import message_bad_words_detect
# Events
from .events.link_check import bad_link
from .events.main_events import on_user_event
from .events.mention_check import mention

dp.register_message_handler(
	on_user_event, 
	content_types=[
		types.ContentType.NEW_CHAT_PHOTO, 
		types.ContentType.NEW_CHAT_MEMBERS,
		types.ContentType.LEFT_CHAT_MEMBER,
		types.ContentType.NEW_CHAT_TITLE,
		types.ContentType.DELETE_CHAT_PHOTO,
		types.ContentType.PINNED_MESSAGE,
		types.ContentType.NEW_CHAT_TITLE,
	]
)

dp.register_message_handler(report_command, commands=["report"])

dp.register_message_handler(mention, is_mention=True)

dp.register_message_handler(message_bad_words_detect)
dp.register_message_handler(bad_link)

dp.register_callback_query_handler(report_callback, lambda c: c.data.startswith('report'), is_admin=True)
