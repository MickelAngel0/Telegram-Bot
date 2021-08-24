from datetime import time
from constants import IMAGE_SCHEDULER, TEXT_SCHEDULER
from Bot.sendTextOrEmoji import sendTextOrEmoji
from Bot.sendImage import sendImage
from telegram import Update
from telegram.ext import CallbackContext
from Database import admin
import pytz


def start(update: Update, context: CallbackContext) -> None:
    """Sends explanation on how to use the bot."""

    admin.chatId = update.message.chat_id

    update.message.reply_text(
        "Hi!"
        + "ChatId Successfully Set"
        + "\nUse /image <seconds> to set a timer for Images"
        + "\nUse /text <seconds> to set a timer for Text/Links"
    )


def setTextPostTime(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chatId = update.message.chat_id

    try:
        print(f"Args: {context.args}")

        hour, minute = None, None

        if len(context.args) == 2:
            hour = int(context.args[0])
            minute = int(context.args[1])

        else:
            hour = int(context.args[0])
            minute = 0

        if hour < 0 or minute < 0:
            update.message.reply_text("Sorry we can not go back to future!")
            return

        admin.textPostHour = hour
        admin.textPostMinute = minute

        admin.chatId = chatId
        name = TEXT_SCHEDULER + str(chatId)

        timeToSet = time(hour=hour, minute=minute, tzinfo=pytz.timezone("Asia/Kolkata"))
        print(f"Time Set: {timeToSet}, {timeToSet.tzinfo}, {timeToSet.tzname()}")

        job = context.job_queue.run_daily(sendTextOrEmoji, time=timeToSet, name=name)
        # job.enabled = False
        job.job.pause()

        text = "Post time successfully set!"
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("Usage: /text <Hour> <Minute> (in 24Hr Format)")


def setImagePostTime(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chatId = update.message.chat_id

    try:
        hour, minute = None, None

        if len(context.args) == 2:
            hour = int(context.args[0])
            minute = int(context.args[1])

        else:
            hour = int(context.args[0])
            minute = 0

        if hour < 0 or minute < 0:
            update.message.reply_text("Sorry we can not go back to future!")
            return

        admin.imagePostHour = hour
        admin.imagePostMinute = minute

        admin.chatId = chatId
        name = IMAGE_SCHEDULER + str(chatId)

        timeToSet = time(hour=hour, minute=minute, tzinfo=pytz.timezone("Asia/Kolkata"))
        print(f"Time Set: {timeToSet}, {timeToSet.tzinfo}, {timeToSet.tzname()}")

        job = context.job_queue.run_daily(sendImage, time=timeToSet, name=name)
        # job.enabled = False
        job.job.pause()

        text = "Post time successfully set!"
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("Usage: /image <Hour> <Minute> (in 24Hr Format)")


def resetDailyPostTime(update: Update, context: CallbackContext) -> None:
    """Remove the job if the user changed their mind."""
    # chatId = update.message.chat_id
    jobRemoved = removeAllJobs(context)
    text = (
        "Timer successfully cancelled!" if jobRemoved else "You have no active timer."
    )
    update.message.reply_text(text)


def resetTextPostTime(update: Update, context: CallbackContext) -> None:
    """Remove the job if the user changed their mind."""
    chatId = update.message.chat_id
    jobRemoved = removeJobIfExists(TEXT_SCHEDULER + str(chatId), context)
    text = (
        "Text Timer successfully cancelled!"
        if jobRemoved
        else "You have no active Text Post Job."
    )
    update.message.reply_text(text)


def resetImagePostTime(update: Update, context: CallbackContext) -> None:
    """Remove the job if the user changed their mind."""
    chatId = update.message.chat_id
    jobRemoved = removeJobIfExists(IMAGE_SCHEDULER + str(chatId), context)
    text = (
        "Image Timer successfully cancelled!"
        if jobRemoved
        else "You have no active Image Post Job."
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


def removeAllJobs(context: CallbackContext) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.jobs()
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True
