from telegram.ext.jobqueue import Job
from constants import TEXT_SCHEDULER
import logging
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from Bot import admin


def sendTextOrEmoji(context: CallbackContext) -> None:
    logging.info("SENDING TEXT/YOUTUBE LINK:")

    if len(admin.scheduledYoutubeLinks) != 0:
        scheduledYoutubeLink = admin.scheduledYoutubeLinks.pop(0)

        logging.info("SuperGrps:")

        for superGrpChatId in admin.superGroups:
            result = context.bot.send_message(
                chat_id=superGrpChatId,
                text=scheduledYoutubeLink.text,
                entities=scheduledYoutubeLink.entities,
            )

            print(f"{superGrpChatId} : {result.message_id}")
            admin.sentMessages[superGrpChatId][
                scheduledYoutubeLink.message_id
            ] = result.message_id
            print("Admin Sent Msgs:", admin.sentMessages)

        context.bot.sendMessage(
            scheduledYoutubeLink.chat_id,
            text="Successfully Posted",
            reply_to_message_id=scheduledYoutubeLink.message_id,
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

        if len(admin.scheduledYoutubeLinks) == 0:
            print('Length of scheduled text is 0')
            job = context.job_queue.get_jobs_by_name(TEXT_SCHEDULER + str(admin.chatId))[0]
        
            job.job.pause()
            print("Job: " + TEXT_SCHEDULER + str(admin.chatId) + " Paused")

    else:
        print("Else Part")
        job = context.job_queue.get_jobs_by_name(TEXT_SCHEDULER + str(admin.chatId))[0]
        print(job)
        print("Default Enabled Val:", job.enabled)

        # job.enabled = ~job.enabled
        # print("Inverted:", job.enabled)

        # job.enabled = False
        # print("Set to false:", job.enabled)

        # job.enabled = True
        # print("Set to true:", job.enabled)

        # if job.enabled == True:
        # job.enabled = False
        job.job.pause()
        print("Job: " + TEXT_SCHEDULER + str(admin.chatId) + " Disabled")

        print("After setting enable: ", job.enabled)
        print("Else Part Complete")

    # print("Remaining MSGS:", admin.scheduledYoutubeLinks)
