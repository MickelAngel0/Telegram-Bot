import logging
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import updater
from Database import admin


def sendScheduledTextOrEmoji() -> None:
    logging.info("SENDING TEXT/YOUTUBE LINK:")

    if len(admin.scheduledYoutubeLinks) != 0:
        scheduledYoutubeLink = admin.scheduledYoutubeLinks.pop(0)

        logging.info("SuperGrps:")

        for superGrpChatId in admin.superGroups:
            result = updater.bot.send_message(
                chat_id=superGrpChatId,
                text=scheduledYoutubeLink.text,
                entities=scheduledYoutubeLink.entities,
            )

            print(f"{superGrpChatId} : {result.message_id}")
            admin.sentMessages[str(superGrpChatId)][
                str(scheduledYoutubeLink.message_id)
            ] = result.message_id
            print("Admin Sent Msgs:", admin.sentMessages)

        updater.bot.sendMessage(
            scheduledYoutubeLink.chat_id,
            text=f"Successfully Posted\nRemaining Posts: {len(admin.scheduledYoutubeLinks)}",
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
        print("Else Part")
        print("No Posts to share")

    admin.writeToFile()


sendScheduledTextOrEmoji()
