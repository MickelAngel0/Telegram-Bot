from datetime import time
import telegram
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.keyboardbutton import KeyboardButton
from constants import BOT_TOKEN
import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


# def sendPic(context: CallbackContext) -> None:
#     """Send the alarm message."""
#     job = context.job
#     context.bot.send_photo(
#         job.context.chat_id,
#         photo=job.context.photo[-1].file_id,
#         caption=job.context.caption,
#         caption_entities=job.context.caption_entities,
#     )

# def recievePic(update: Update, context: CallbackContext) -> None:
#     """Add a job to the queue."""
#     chat_id = update.message.chat_id

#     try:
#         job_removed = remove_job_if_exists(str(chat_id), context)
#         context.job_queue.run_once(
#             sendPic, dueTime, context=update.message, name=str(chat_id)
#         )

#         text = "Timer successfully set!"
#         if job_removed:
#             text += " Old one was removed."
#         update.message.reply_text(text)

#     except (IndexError, ValueError):
#         update.message.reply_text("Usage: /set <seconds>")


class Admin:
    def __init__(self) -> None:
        self.chatId = None
        self.scheduledMessages: list[telegram.Message] = []
        self.dueTime = 15
        self.sentMessages: dict[int, int] = {}


admin = Admin()


def start(update: Update, context: CallbackContext) -> None:
    """Sends explanation on how to use the bot."""
    update.message.reply_text("Hi! Use /set <seconds> to set a timer")


def sendText(context: CallbackContext) -> None:
    """Send the alarm message."""
    job = context.job
    if len(admin.scheduledMessages) != 0:
        scheduledMsg = admin.scheduledMessages.pop(0)
        result = context.bot.send_message(scheduledMsg.chat_id, text=scheduledMsg.text)

        print("RES after sending in channels", result.message_id)
        admin.sentMessages[scheduledMsg.message_id] = result.message_id

        context.bot.sendMessage(
            scheduledMsg.chat_id,
            text="Successfully Posted",
            reply_to_message_id=result.message_id - 2,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Delete",
                            callback_data="delete",
                        ),
                        # InlineKeyboardButton(
                        #     text="Edit",
                        #     callback_data={"edit": scheduledMsg.message_id},
                        # ),
                    ]
                ]
            )
            # reply_markup=ReplyKeyboardMarkup(
            #     keyboard=[[KeyboardButton(text="Delete"), KeyboardButton(text="Edit")]],
            # ),
        )
    else:

        job = context.job_queue.get_jobs_by_name(str(admin.chatId))[0]
        if job.enabled is True:
            job.enabled = False


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def set_timer(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id

    try:
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text("Sorry we can not go back to future!")
            return

        admin.dueTime = due
        admin.chatId = chat_id

        job = context.job_queue.run_repeating(
            sendText, admin.dueTime, name=str(chat_id)
        )
        job.enabled = False

        text = "DueTime successfully set!"
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("Usage: /set <seconds>")


def recieveText(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.effective_message.chat_id

    try:

        if update.edited_message:
            print("edited msg")
            print(update.edited_message.message_id)

            if any(
                item.message_id == update.edited_message.message_id
                for item in admin.scheduledMessages
            ):
                print("in sch msgs")

                for index, item in enumerate(admin.scheduledMessages):
                    if item.message_id == update.edited_message.message_id:
                        admin.scheduledMessages[index] = update.edited_message
                        break

            elif update.edited_message.message_id in admin.sentMessages:

                context.bot.edit_message_text(
                    text=update.edited_message.text,
                    chat_id=chat_id,
                    message_id=admin.sentMessages[update.edited_message.message_id],
                    entities=update.edited_message.entities,
                )

        else:

            admin.scheduledMessages.append(update.message)
            print("added new msg to sch ", update.message.message_id)
            job = context.job_queue.get_jobs_by_name(str(chat_id))[0]

            if job.enabled != True:
                job.enabled = True

            text = "Text successfully added!"
            update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("MSG: No Job present, please set time first")


def unset(update: Update, context: CallbackContext) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = (
        "Timer successfully cancelled!" if job_removed else "You have no active timer."
    )
    update.message.reply_text(text)


# def printMessage(update: Update, context: CallbackContext) -> None:
#     print("Print Message")
#     print(update.message)


def callback(update: Update, context: CallbackContext) -> None:
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


def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    # dispatcher.add_handler(MessageHandler(Filters.all, printMessage))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("set", set_timer))
    dispatcher.add_handler(CommandHandler("unset", unset))
    dispatcher.add_handler(CallbackQueryHandler(callback))
    dispatcher.add_handler(MessageHandler(Filters.text, recieveText))
    # dispatcher.add_handler(MessageHandler(Filters.photo, recievePic))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
