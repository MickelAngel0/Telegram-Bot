from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaAnimation


def animation(update: Update, context: CallbackContext):

    if update.edited_message:
        context.bot.edit_message_media(
            media=InputMediaAnimation(
                media=update.edited_message.animation,
                caption=update.edited_message.caption,
                caption_entities=update.edited_message.caption_entities,
                filename=update.edited_message.animation.file_name,
                thumb=update.edited_message.animation.thumb,
            ),
            chat_id=update.edited_message.chat_id,
            message_id=update.edited_message.message_id + 1,
        )

    else:
        context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=update.message.animation.file_id,
            duration=update.message.animation.duration,
            width=update.message.animation.width,
            height=update.message.animation.height,
            thumb=update.message.animation.thumb,
            caption=update.message.caption,
            caption_entities=update.message.caption_entities,
            filename=update.message.animation.file_name,
        )
