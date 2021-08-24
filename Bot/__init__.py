from constants import BOT_TOKEN
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler, CallbackQueryHandler


updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher
jobQueue = updater.job_queue

from .commands import *
from .errorHandler import errorHandler
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

dispatcher.add_handler(
    MessageHandler(Filters.text & Filters.chat(1530597878), recieveTextOrEmoji)
)
dispatcher.add_handler(
    MessageHandler(Filters.photo & Filters.chat(1530597878), recieveImage)
)
dispatcher.add_handler(
    MessageHandler(
        Filters.video & Filters.chat_type.private,
        recieveVideo,
    )
)
dispatcher.add_handler(
    MessageHandler(Filters.audio & Filters.chat_type.private, recieveAudio)
)
dispatcher.add_handler(
    MessageHandler(Filters.sticker & Filters.chat_type.private, recieveSticker)
)
dispatcher.add_handler(
    MessageHandler(Filters.animation & Filters.chat_type.private, recieveAnimationOrGif)
)
dispatcher.add_handler(
    MessageHandler(Filters.document & Filters.chat_type.private, recieveDocument)
)
# dispatcher.add_handler(MessageHandler(Filters.poll, poll))

dispatcher.add_error_handler(errorHandler)
