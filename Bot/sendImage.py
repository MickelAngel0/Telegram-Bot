from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaPhoto
import logging


def sendImage(update: Update, context: CallbackContext):

    logging.info("SENDING IMAGE:")

    if update.edited_message:
        # print("if part")

        # Works
        # context.bot.edit_message_caption(
        #     # media=InputMediaPhoto(update.message.photo[-1].file_id),
        #     caption=update.effective_message.caption,
        #     # text=update.effective_message.text,
        #     chat_id=update.effective_chat.id,
        #     message_id=update.effective_message.message_id + 1,
        #     caption_entities=update.effective_message.caption_entities,
        # )

        context.bot.edit_message_media(
            media=InputMediaPhoto(
                media=update.effective_message.photo[-1].file_id,
                caption=update.effective_message.caption,
                caption_entities=update.effective_message.caption_entities,
                # filename=update.edited_message.photo[-1],
            ),
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id + 1,
        )

        # context.bot.editMessageCaption
    else:
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=update.effective_message.photo[-1].file_id,
            caption=update.effective_message.caption,
            # filename= update.message.photo[-1],
            caption_entities=update.effective_message.caption_entities,
        )
