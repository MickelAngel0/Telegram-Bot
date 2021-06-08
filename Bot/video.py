from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaVideo


def video(update: Update, context: CallbackContext):
    if update.edited_message:
        print("if part")

        context.bot.edit_message_media(
            media=InputMediaVideo(
                media=update.edited_message.video,
                caption=update.edited_message.caption,
                caption_entities=update.edited_message.caption_entities,
                filename=update.edited_message.video.file_name,
                # thumb=update.edited_message.video.thumb,
            ),
            chat_id=update.edited_message.chat_id,
            message_id=update.edited_message.message_id + 1,
        )
    else:
        context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=update.message.video.file_id,
            caption=update.message.caption,
            caption_entities=update.message.caption_entities,
            filename=update.message.video.file_name,
            duration=update.message.video.duration,
            width=update.message.video.width,
            height=update.message.video.height,
            # thumb=update.message.video.thumb,
        )
