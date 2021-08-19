from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from Bot import admin


def sendTextOrEmoji(update: Update, context: CallbackContext) -> None:
    """Send the alarm message."""
    job = context.job
    if len(admin.scheduledMessages) != 0:
        scheduledMsg = admin.scheduledMessages.pop(0)
        result = context.bot.send_message(scheduledMsg.chat_id, text=scheduledMsg.text)

        print("RES after sending in channels", result.message_id)
        admin.sentMessages[scheduledMsg.message_id] = result.message_id

        context.bot.sendMessage(
            scheduledMsg.chat_id,
            text="Successfully Posted",
            reply_to_message_id=result.message_id - 2,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Delete",
                            callback_data="delete",
                        ),
                        # InlineKeyboardButton(
                        #     text="Edit",
                        #     callback_data={"edit": scheduledMsg.message_id},
                        # ),
                    ]
                ]
            ),
        )
    else:

        job = context.job_queue.get_jobs_by_name(str(admin.chatId))[0]
        if job.enabled is True:
            job.enabled = False
