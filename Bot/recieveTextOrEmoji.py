from constants import CHANNELS, MESSAGESPOSTED, SUBSCRIBERS, SUPERGROUPS
from telegram import Update, bot
import telegram
from telegram.ext import CallbackContext
from Bot import botData


def recieveTextOrEmoji(update: Update, context: CallbackContext):

    print("TEXT OR EMOJI:")

    if update.edited_message:
        print("EDIT:")

        botData.editScheduledMessage(
            userId=update.effective_chat.id,
            messageId=update.effective_message.message_id,
            newMessage=update.effective_message.to_dict(),
        )

        # for chatId in botData.botData[update.effective_chat.id][CHANNELS]:
        #     context.bot.edit_message_text(
        #         text=update.effective_message.text,
        #         chat_id=chatId,
        #         message_id=botData.botData[update.effective_chat.id][MESSAGESPOSTED][
        #             chatId
        #         ],
        #         entities=update.effective_message.entities,
        #     )

        # for chatId in botData.botData[update.effective_chat.id][SUPERGROUPS]:
        #     context.bot.edit_message_text(
        #         text=update.effective_message.text,
        #         chat_id=chatId,
        #         message_id=botData.botData[update.effective_chat.id][MESSAGESPOSTED][
        #             chatId
        #         ],
        #         entities=update.effective_message.entities,
        #     )
    else:
        print("SEND:")

        # botData.saveMessageToPickle(update.effective_message.to_dict())
        botData.scheduleMessage(
            userId=update.effective_chat.id,
            messageId=update.effective_message.message_id,
            message=update.effective_message.to_dict(),
        )

        # messageDict = {}

        # for chatId in botData.botData[update.effective_chat.id][CHANNELS]:
        #     print("CHANNEL CHATID:", chatId)
        #     # print(update.effective_chat.type == telegram.Chat.CHANNEL)

        #     resultMessage = context.bot.send_message(
        #         chat_id=chatId,
        #         text=update.effective_message.text,
        #         # disable_web_page_preview=update.message.text,
        #         entities=update.effective_message.entities,
        #     )
        #     messageDict[chatId] = resultMessage.message_id

        # for chatId in botData.botData[update.effective_chat.id][SUPERGROUPS]:
        #     print("SUPERGROUP CHATID:", chatId)
        #     # print(update.effective_chat.type == telegram.Chat.SUPERGROUP)

        #     resultMessage = context.bot.send_message(
        #         chat_id=chatId,
        #         text=update.effective_message.text,
        #         # disable_web_page_preview=update.message.text,
        #         entities=update.effective_message.entities,
        #     )
        #     messageDict[chatId] = resultMessage.message_id

        # botData.botData[update.effective_chat.id][MESSAGESPOSTED] = messageDict
        # # messageIds[update.effective_message.message_id] = messageDict
        # print("BOTDATA:", botData.botData)
        # botData.writeDataToFile()


def sendTextOrEmoji(context: CallbackContext, message: telegram.Message, userId: int):
    print("SEND TEXT OR EMOJI:")

    messageDict = {}

    for chatId in botData.botData[userId][CHANNELS]:
        # print("CHANNEL CHATID:", chatId)

        resultMessage = context.bot.send_message(
            chat_id=chatId,
            text=message.text,
            # disable_web_page_preview=update.message.text,
            entities=message.entities,
        )
        messageDict[chatId] = resultMessage.message_id

    for chatId in botData.botData[userId][SUPERGROUPS]:
        # print("SUPERGROUP CHATID:", chatId)

        resultMessage = context.bot.send_message(
            chat_id=chatId,
            text=message.text,
            # disable_web_page_preview=update.message.text,
            entities=message.entities,
        )
        messageDict[chatId] = resultMessage.message_id

    for chatId in botData.botData[userId][SUBSCRIBERS]:
        # print("SUPERGROUP CHATID:", chatId)

        resultMessage = context.bot.send_message(
            chat_id=chatId,
            text=message.text,
            # disable_web_page_preview=update.message.text,
            entities=message.entities,
        )
        messageDict[chatId] = resultMessage.message_id

    botData.addPostedMessages(
        userId=userId,
        userMessageId=message.message_id,
        postedMessageIds=messageDict,
    )

    # botData.botData[update.effective_chat.id][MESSAGESPOSTED] = messageDict
    # # messageIds[update.effective_message.message_id] = messageDict
    # print("BOTDATA:", botData.botData)
    botData.writeDataToFile()
