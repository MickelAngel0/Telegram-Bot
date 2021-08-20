from telegram.ext import CallbackContext
import logging
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import admin


def sendImage(context: CallbackContext):
    logging.info("SENDING IMAGE:")

    if len(admin.scheduledImages) != 0:
        scheduledImage = admin.scheduledImages.pop(0)

        logging.info("SuperGrps:")

        for superGrpChatId in admin.superGroups:
            result = context.bot.send_photo(
                chat_id=superGrpChatId,
                photo=scheduledImage.photo[-1].file_id,
                caption=scheduledImage.caption,
                caption_entities=scheduledImage.caption_entities,
            )

            print(f"{superGrpChatId} : {result.message_id}")
            admin.sentMessages[superGrpChatId][
                scheduledImage.message_id
            ] = result.message_id

        context.bot.sendMessage(
            chat_id=scheduledImage.chat_id,
            text="Successfully Posted",
            reply_to_message_id=scheduledImage.message_id,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Delete",
                            callback_data="Delete",
                        ),
                    ]
                ]
            ),
        )

    else:
        job = context.job_queue.get_jobs_by_name(str(admin.chatId))[0]
        if job.enabled is True:
            job.enabled = False

    # if update.edited_message:
    #     # print("if part")

    #     # Works
    #     # context.bot.edit_message_caption(
    #     #     # media=InputMediaPhoto(update.message.photo[-1].file_id),
    #     #     caption=update.effective_message.caption,
    #     #     # text=update.effective_message.text,
    #     #     chat_id=update.effective_chat.id,
    #     #     message_id=update.effective_message.message_id + 1,
    #     #     caption_entities=update.effective_message.caption_entities,
    #     # )

    #     context.bot.edit_message_media(
    #         media=InputMediaPhoto(
    #             media=update.effective_message.photo[-1].file_id,
    #             caption=update.effective_message.caption,
    #             caption_entities=update.effective_message.caption_entities,
    #             # filename=update.edited_message.photo[-1],
    #         ),
    #         chat_id=update.effective_chat.id,
    #         message_id=update.effective_message.message_id + 1,
    #     )

    #     # context.bot.editMessageCaption
    # else:
    #     context.bot.send_photo(
    #         chat_id=update.effective_chat.id,
    #         photo=update.effective_message.photo[-1].file_id,
    #         caption=update.effective_message.caption,
    #         # filename= update.message.photo[-1],
    #         caption_entities=update.effective_message.caption_entities,
    #     )
