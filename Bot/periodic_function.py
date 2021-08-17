from telegram import message
from Bot.text import sendTextOrEmoji
import telegram
from constants import (
    CHANNELS,
    MESSAGESPOSTED,
    MESSAGESSCHEDULED,
    MESSAGETYPETEXT,
    SUPERGROUPS,
)
from telegram.ext.callbackcontext import CallbackContext
from Bot import botData


def periodic(context: CallbackContext):

    # messageDict = {}
    if len(botData.botData[1530597878][MESSAGESSCHEDULED]) == 0:
        print("No Data In Job")
    else:

        telegramMessage = telegram.Message.de_json(
            botData.botData[1530597878][MESSAGESSCHEDULED][0],
            bot=context.bot,
        )

        if (
            botData.botData[1530597878][MESSAGESSCHEDULED][0]["messageType"]
            == MESSAGETYPETEXT
        ):
            sendTextOrEmoji(context=context, message=telegramMessage, userId=1530597878)

        # for chatId in botData.botData[1530597878][CHANNELS]:
        #     print("CHANNEL CHATID:", chatId)

        #     resultMessage = context.bot.send_message(
        #         chat_id=chatId,
        #         text=telegramMessage.text,
        #         # disable_web_page_preview=update.message.text,
        #         entities=telegramMessage.entities,
        #     )
        #     messageDict[chatId] = resultMessage.message_id

        # for chatId in botData.botData[1530597878][SUPERGROUPS]:
        #     print("SUPERGROUP CHATID:", chatId)

        #     resultMessage = context.bot.send_message(
        #         chat_id=chatId,
        #         text=telegramMessage.text,
        #         # disable_web_page_preview=update.message.text,
        #         entities=telegramMessage.entities,
        #     )
        #     messageDict[chatId] = resultMessage.message_id

        # botData.botData[1530597878][MESSAGESPOSTED] = messageDict

        # botData.removeFirstMessageFromSceduledMessages()

        # # messageIds[update.effective_message.message_id] = messageDict
        # print("BOTDATA:", botData.botData)
        # botData.writeDataToFile()
