from telegram import Update
from telegram.ext import CallbackContext
from telegram.files.inputmedia import InputMediaPhoto
import logging
from Bot import admin


def recieveImage(update: Update, context: CallbackContext):
    logging.info("RECIEVED IMAGE:")

    try:
        if update.edited_message:
            print("It is a Edited Image/Caption")

            if any(
                item.message_id == update.edited_message.message_id
                for item in admin.scheduledImages
            ):
                print("Present in Scheduled Msgs")

                for index, msg in enumerate(admin.scheduledImages):
                    if msg.message_id == update.edited_message.message_id:
                        admin.scheduledImages[index] = update.edited_message
                        break

            elif any(
                keyVal.__contains__(update.edited_message.message_id)
                for keyVal in admin.sentMessages.values()
            ):
                print("Present in Sent Msgs")

                for superGrpChatId in admin.superGroups:
                    context.bot.edit_message_media(
                        media=InputMediaPhoto(
                            media=update.edited_message.photo[-1].file_id,
                            caption=update.edited_message.caption,
                            caption_entities=update.edited_message.caption_entities,
                            # filename=update.edited_message.photo[-1],
                        ),
                        chat_id=superGrpChatId,
                        message_id=admin.sentMessages[superGrpChatId][
                            update.edited_message.message_id
                        ],
                    )

                    # context.bot.edit_message_caption(
                    #     # media=InputMediaPhoto(update.message.photo[-1].file_id),
                    #     caption=update.edited_message.caption,
                    #     # text=update.effective_message.text,
                    #     chat_id=superGrpChatId,
                    #     message_id=admin.sentMessages[superGrpChatId][
                    #         update.edited_message.message_id
                    #     ],
                    #     caption_entities=update.edited_message.caption_entities,
                    # )

        else:
            chatId = update.effective_message.chat_id
            admin.scheduledImages.append(update.message)

            logging.info(f"Scheduled the Msg: {update.message.message_id}")
            job = context.job_queue.get_jobs_by_name(str(chatId))[0]

            if job.enabled != True:
                job.enabled = True

            text = "Image successfully Scheduled!"
            update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("No Job present, Please set time first")
