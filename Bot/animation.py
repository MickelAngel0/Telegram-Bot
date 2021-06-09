from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaAnimation


def animation(update: Update, context: CallbackContext):

    if update.edited_message:
        context.bot.edit_message_media(
            media=InputMediaAnimation(
                media=update.effective_message.animation.file_id,
                caption=update.effective_message.caption,
                caption_entities=update.effective_message.caption_entities,
                filename=update.effective_message.animation.file_name,
                thumb=update.effective_message.animation.thumb,
            ),
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id + 1,
        )

    else:
        context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=update.effective_message.animation.file_id,
            duration=update.effective_message.animation.duration,
            width=update.effective_message.animation.width,
            height=update.effective_message.animation.height,
            thumb=update.effective_message.animation.thumb,
            caption=update.effective_message.caption,
            caption_entities=update.effective_message.caption_entities,
            filename=update.effective_message.animation.file_name,
        )
