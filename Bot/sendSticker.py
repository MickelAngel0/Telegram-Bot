from telegram import Update
from telegram.ext import CallbackContext


def sendSticker(update: Update, context: CallbackContext):
    print('STICKER:')
    
    # if update.edited_message:
    #     print("if part")

    #     context.bot.edit_message_media(
    #         media=InputMedia(
    #             media=update.edited_message.audio,
    #             caption=update.edited_message.caption,
    #             caption_entities=update.edited_message.caption_entities,
    #             # filename=update.message.photo[-1].,
    #         ),
    #         # text=update.effective_message.text,
    #         chat_id=update.edited_message.chat_id,
    #         message_id=update.edited_message.message_id + 1,
    #     )
    # else:

    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker=update.effective_message.sticker.file_id,
    )
