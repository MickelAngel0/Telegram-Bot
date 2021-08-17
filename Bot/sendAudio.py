from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaAudio
import logging


def sendAudio(update: Update, context: CallbackContext):
    logging.info('SENDING AUDIO:')

    if update.edited_message:
        context.bot.edit_message_media(
            media=InputMediaAudio(
                media=update.effective_message.audio.file_id,
                caption=update.effective_message.caption,
                caption_entities=update.effective_message.caption_entities,
                filename=update.effective_message.audio.file_name,
                thumb=update.effective_message.audio.thumb,
                title=update.effective_message.audio.title,
            ),
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id + 1,
        )

    else:
        context.bot.send_audio(
            chat_id=update.effective_chat.id,
            audio=update.effective_message.audio.file_id,
            title=update.effective_message.audio.title,
            filename=update.effective_message.audio.file_name,
            duration=update.effective_message.audio.duration,
            caption=update.effective_message.caption,
            thumb=update.effective_message.audio.thumb,
            caption_entities=update.effective_message.caption_entities,
        )
