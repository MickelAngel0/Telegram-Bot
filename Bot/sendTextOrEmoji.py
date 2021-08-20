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
            print('Admin Sent Msgs:', admin.sentMessages)

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

    else:
        job = context.job_queue.get_jobs_by_name(str(admin.chatId))[0]
        if job.enabled is True:
            job.enabled = False
