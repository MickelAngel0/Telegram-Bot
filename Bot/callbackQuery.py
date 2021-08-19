from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext


def callbackQuery(update: Update, context: CallbackContext) -> None:
    print("Print Message")
    # print(update.effective_message)
    query = update.callback_query

    # THis shows a notification
    query.answer("You selected ", query.data)

    query.edit_message_text(
        query.data,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Done",
                        callback_data="delete",
                    ),
                ]
            ]
        ),
    )
