from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaAudio


def audio(update: Update, context: CallbackContext):
    if update.edited_message:
        context.bot.edit_message_media(
            media=InputMediaAudio(
                media=update.edited_message.audio,
                caption=update.edited_message.caption,
                caption_entities=update.edited_message.caption_entities,
                filename=update.edited_message.audio.file_name,
                thumb=update.edited_message.audio.thumb,
                title=update.edited_message.audio.title,
            ),
            chat_id=update.edited_message.chat_id,
            message_id=update.edited_message.message_id + 1,
        )

    else:
        context.bot.send_audio(
            chat_id=update.effective_chat.id,
            audio=update.message.audio.file_id,
            title=update.message.audio.title,
            filename=update.message.audio.file_name,
            duration=update.message.audio.duration,
            caption=update.message.caption,
            thumb=update.message.audio.thumb,
            caption_entities=update.message.caption_entities,
        )
