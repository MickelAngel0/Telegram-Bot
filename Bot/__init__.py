from datetime import datetime
from botData import BotData
from constants import BOT_TOKEN
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

botData = BotData()

updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher
jobQueue = updater.job_queue

from .command import start
from .animation import animationOrGif
from .audio import audio
from .document import document
from .photo import photo
from .poll import poll
from .sticker import sticker
from .text import textOrEmoji
from .video import video

from .periodic_function import periodic


# dispatcher.add_handler(
#     MessageHandler(Filters.chat_type.channel | Filters.chat_type.supergroup, ())
# )


# jobQueue.run_repeating(periodic, interval=10, first=10)
# jobQueue.run_daily(periodic, datetime.utcnow())

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.text, textOrEmoji))
dispatcher.add_handler(MessageHandler(Filters.photo, photo))
dispatcher.add_handler(MessageHandler(Filters.video, video))
dispatcher.add_handler(MessageHandler(Filters.audio, audio))
dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))
dispatcher.add_handler(MessageHandler(Filters.animation, animationOrGif))
dispatcher.add_handler(MessageHandler(Filters.poll, poll))
dispatcher.add_handler(MessageHandler(Filters.document, document))
