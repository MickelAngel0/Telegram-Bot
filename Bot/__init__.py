from constants import BOT_TOKEN
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler, CallbackQueryHandler


updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher
jobQueue = updater.job_queue

from .commands import *
from .callbackQuery import callbackQuery
from .recieveAnimationOrGif import recieveAnimationOrGif
from .recieveAudio import recieveAudio
from .recieveDocument import recieveDocument
from .recieveImage import recieveImage
from .recieveSticker import recieveSticker
from .recieveTextOrEmoji import recieveTextOrEmoji
from .recieveVideo import recieveVideo


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", start))
dispatcher.add_handler(CommandHandler("text", setTextPostTime))
dispatcher.add_handler(CommandHandler("image", setImagePostTime))
dispatcher.add_handler(CommandHandler("resetText", resetTextPostTime))
dispatcher.add_handler(CommandHandler("resetImage", resetImagePostTime))
dispatcher.add_handler(CommandHandler("resetAll", resetDailyPostTime))
dispatcher.add_handler(CallbackQueryHandler(callbackQuery))

dispatcher.add_handler(MessageHandler(Filters.text, recieveTextOrEmoji))
dispatcher.add_handler(MessageHandler(Filters.photo, recieveImage))
dispatcher.add_handler(MessageHandler(Filters.video, recieveVideo))
dispatcher.add_handler(MessageHandler(Filters.audio, recieveAudio))
dispatcher.add_handler(MessageHandler(Filters.sticker, recieveSticker))
dispatcher.add_handler(MessageHandler(Filters.animation, recieveAnimationOrGif))
# dispatcher.add_handler(MessageHandler(Filters.poll, poll))
dispatcher.add_handler(MessageHandler(Filters.document, recieveDocument))
