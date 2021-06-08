from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaDocument


def document(update: Update, context: CallbackContext):
    if update.edited_message:
        print("if part")

        context.bot.edit_message_media(
            media=InputMediaDocument(
                media=update.edited_message.document,
                caption=update.edited_message.caption,
                caption_entities=update.edited_message.caption_entities,
                filename=update.edited_message.document.file_name,
                # thumb=update.edited_message.document.thumb,
            ),
            chat_id=update.edited_message.chat_id,
            message_id=update.edited_message.message_id + 1,
        )
    else:
        context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=update.message.document.file_id,
            filename=update.message.document.file_name,
            caption=update.message.caption,
            # thumb=update.message.document.thumb,
            caption_entities=update.message.caption_entities,
        )
