from telegram import Update
from telegram.ext import CallbackContext
# from telegram.files.inputmedia import InputMediaVideo
import logging


def recieveVideo(update: Update, context: CallbackContext):
    logging.info("RECIEVED VIDEO:")

    update.message.reply_text(
        "Cannot handle this media at the point,\nPlease try again later."
    )

    # if update.edited_message:
    #     # print("if part")

    #     context.bot.edit_message_media(
    #         media=InputMediaVideo(
    #             media=update.effective_message.video.file_id,
    #             caption=update.effective_message.caption,
    #             caption_entities=update.effective_message.caption_entities,
    #             filename=update.effective_message.video.file_name,
    #             # thumb=update.edited_message.video.thumb,
    #         ),
    #         chat_id=update.effective_chat.id,
    #         message_id=update.effective_message.message_id + 1,
    #     )
    # else:
    #     context.bot.send_video(
    #         chat_id=update.effective_chat.id,
    #         video=update.effective_message.video.file_id,
    #         caption=update.effective_message.caption,
    #         caption_entities=update.effective_message.caption_entities,
    #         filename=update.effective_message.video.file_name,
    #         # duration=update.effective_message.video.duration,
    #         # width=update.effective_message.video.width,
    #         # height=update.effective_message.video.height,
    #         # thumb=update.message.video.thumb,
    #     )
