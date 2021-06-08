from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaPhoto


def photo(update: Update, context: CallbackContext):

    print(update)

    if update.edited_message:
        print("if part")

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
                media=update.edited_message.photo[-1].file_id,
                caption=update.edited_message.caption,
                caption_entities=update.edited_message.caption_entities,
                # filename=update.edited_message.photo[-1],
            ),
            chat_id=update.edited_message.chat_id,
            message_id=update.edited_message.message_id + 1,
        )

        # context.bot.editMessageCaption
    else:
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=update.message.photo[-1].file_id,
            caption=update.message.caption,
            # filename= update.message.photo[-1],
            caption_entities=update.message.caption_entities,
        )
