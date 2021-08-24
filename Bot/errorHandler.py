from constants import TEXT_SCHEDULER
import logging
from telegram import Update
from telegram.ext import CallbackContext
from Database import admin


def errorHandler(update: Update, context: CallbackContext) -> None:
    logging.info("RECIEVED SOME ERROR:")

    update.message.reply_text("Some Error Occured")
