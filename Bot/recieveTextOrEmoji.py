from constants import TEXT_SCHEDULER
import logging
from telegram import Update
from telegram.ext import CallbackContext
from Bot import admin


def recieveTextOrEmoji(update: Update, context: CallbackContext) -> None:
    logging.info("RECIEVED TEXT/YOUTUBE LINK:")

    try:
        if update.edited_message:
            print("It is a Edited Msg")

            if any(
                item.message_id == update.edited_message.message_id
                for item in admin.scheduledYoutubeLinks
            ):
                print("Present in Scheduled Msgs")

                for index, msg in enumerate(admin.scheduledYoutubeLinks):
                    if msg.message_id == update.edited_message.message_id:
                        admin.scheduledYoutubeLinks[index] = update.edited_message
                        break

            elif any(
                keyVal.__contains__(update.edited_message.message_id)
                for keyVal in admin.sentMessages.values()
            ):
                print("Present in Sent Msgs")
                for superGrpChatId in admin.superGroups:
                    context.bot.edit_message_text(
                        text=update.edited_message.text,
                        chat_id=superGrpChatId,
                        message_id=admin.sentMessages[superGrpChatId][
                            update.edited_message.message_id
                        ],
                        entities=update.edited_message.entities,
                    )
            else:
                print("No Condition fulfilled")

        else:
            chatId = update.effective_message.chat_id
            # print("Jobs:", context.job_queue.jobs())

            job = context.job_queue.get_jobs_by_name(TEXT_SCHEDULER + str(chatId))[0]
            print("Job:", job)

            # if job.enabled != True:
            # job.enabled = True

            admin.scheduledYoutubeLinks.append(update.message)
            logging.info(
                f"Scheduled the Msg : {update.message.message_id}, {update.message.text}"
            )

            job.job.resume()

            text = "Text/Youtube Link successfully Scheduled!"
            update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("No Job present, Please set time first")
