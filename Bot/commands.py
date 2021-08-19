from telegram import Update
from telegram.ext import CallbackContext
from Bot import admin
from Bot import sendTextOrEmoji


def start(update: Update, context: CallbackContext) -> None:
    """Sends explanation on how to use the bot."""
    update.message.reply_text("Hi! Use /set <seconds> to set a timer")


def setDailyPostTime(update: Update, context: CallbackContext) -> None:
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
            sendTextOrEmoji, admin.dueTime, name=str(chat_id)
        )
        job.enabled = False

        text = "DueTime successfully set!"
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("Usage: /set <seconds>")


def unsetDailyPostTime(update: Update, context: CallbackContext) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = removeJobIfExists(str(chat_id), context)
    text = (
        "Timer successfully cancelled!" if job_removed else "You have no active timer."
    )
    update.message.reply_text(text)


def removeJobIfExists(name: str, context: CallbackContext) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True
