from telegram import Update
from telegram.ext import CallbackContext


def text(update: Update, context: CallbackContext):

    print(update)

    if update.edited_message:
        print("if part")

        context.bot.edit_message_text(
            text=update.effective_message.text,
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id + 1,
            entities=update.effective_message.entities,
        )
    else:
        print("else part")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=update.effective_message.text,
            # disable_web_page_preview=update.message.text,
            entities=update.effective_message.entities,
        )
