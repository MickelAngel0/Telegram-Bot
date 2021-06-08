from telegram import Update
from telegram.ext import CallbackContext


def text(update: Update, context: CallbackContext):

    update.edited_message

    if update.edited_message:
        print("if part")

        context.bot.edit_message_text(
            text=update.edited_message.text,
            chat_id=update.edited_message.chat_id,
            message_id=update.edited_message.message_id + 1,
            entities=update.edited_message.entities,
        )
    else:
        print("else part")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=update.message.text,
            # disable_web_page_preview=update.message.text,
            entities=update.message.entities,
        )
