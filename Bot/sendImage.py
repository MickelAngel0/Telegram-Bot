from constants import IMAGE_SCHEDULER
from telegram.ext import CallbackContext
import logging
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from Database import admin


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

        if len(admin.scheduledImages) == 0:
            print("Length of scheduled text is 0")
            job = context.job_queue.get_jobs_by_name(
                IMAGE_SCHEDULER + str(admin.chatId)
            )[0]

            job.job.pause()
            print("Job: " + IMAGE_SCHEDULER + str(admin.chatId) + " Paused")

    else:
        print("Else Part")

        job = context.job_queue.get_jobs_by_name(IMAGE_SCHEDULER + str(admin.chatId))[0]
        print(job)
        print("Default Enabled Val:", job.enabled)

        # if job.enabled == True:
        #     job.enabled = False
        #     print("Job: " + IMAGE_SCHEDULER + str(admin.chatId) + "Disabled")

        job.job.pause()
        print("Job: " + IMAGE_SCHEDULER + str(admin.chatId) + " Paused")
