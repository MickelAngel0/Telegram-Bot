from telegram import Update
from telegram.ext import CallbackContext
from Bot import admin


def recieveTextOrEmoji(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.effective_message.chat_id

    try:

        if update.edited_message:
            print("edited msg")
            print(update.edited_message.message_id)

            if any(
                item.message_id == update.edited_message.message_id
                for item in admin.scheduledMessages
            ):
                print("in sch msgs")

                for index, item in enumerate(admin.scheduledMessages):
                    if item.message_id == update.edited_message.message_id:
                        admin.scheduledMessages[index] = update.edited_message
                        break

            elif update.edited_message.message_id in admin.sentMessages:

                context.bot.edit_message_text(
                    text=update.edited_message.text,
                    chat_id=chat_id,
                    message_id=admin.sentMessages[update.edited_message.message_id],
                    entities=update.edited_message.entities,
                )

        else:

            admin.scheduledMessages.append(update.message)
            print("added new msg to sch ", update.message.message_id)
            job = context.job_queue.get_jobs_by_name(str(chat_id))[0]

            if job.enabled != True:
                job.enabled = True

            text = "Text successfully added!"
            update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text("MSG: No Job present, please set time first")
