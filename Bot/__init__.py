from constants import BOT_TOKEN
from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher
jobQueue = updater.job_queue

from .animation import animation
from .audio import audio
from .document import document
from .photo import photo
from .sticker import sticker
from .text import text
from .video import video


dispatcher.add_handler(MessageHandler(Filters.text, text))
dispatcher.add_handler(MessageHandler(Filters.photo, photo))
dispatcher.add_handler(MessageHandler(Filters.video, video))
dispatcher.add_handler(MessageHandler(Filters.audio, audio))
dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))
dispatcher.add_handler(MessageHandler(Filters.animation, animation))
dispatcher.add_handler(MessageHandler(Filters.document, document))
