from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaDocument


def sendDocument(update: Update, context: CallbackContext):
    print('DOCUMENT:')

    if update.edited_message:
        # print("if part")

        context.bot.edit_message_media(
            media=InputMediaDocument(
                media=update.effective_message.document.file_id,
                caption=update.effective_message.caption,
                caption_entities=update.effective_message.caption_entities,
                filename=update.effective_message.document.file_name,
                # thumb=update.edited_message.document.thumb,
            ),
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id + 1,
        )
    else:
        context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=update.effective_message.document.file_id,
            filename=update.effective_message.document.file_name,
            caption=update.effective_message.caption,
            # thumb=update.message.document.thumb,
            caption_entities=update.effective_message.caption_entities,
        )
