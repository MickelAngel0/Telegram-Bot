from datetime import datetime, timedelta
from time import time
import telegram
from telegram.bot import Bot
from telegram.utils.types import JSONDict

from constants import (
    BOTDATAFILENAME,
    CHANNELS,
    DEFAULTSCHEDULETIME,
    MESSAGESPOSTED,
    MESSAGESSCHEDULED,
    SCHEDULETIME,
    SUBSCRIBERS,
    SUPERGROUPS,
)
import pickle, os

timedelta(hours=6, minutes=0)


class BotData:
    def __init__(self) -> None:

        self.readDataFromFile()
        print("Len after init class:", len(self.botData))

    def scheduleMessage(
        self, userId: int, messageId: int, message: JSONDict, messageType: str
    ):
        message["messageId"] = messageId
        message["messageType"] = messageType
        self.botData[userId][MESSAGESSCHEDULED].append(message)
        print("\nMessage Added to schedule List")
        print("BOTDATA After Adding", self.botData)

    def getFirstScheduledMessage(self, userId: int, bot: Bot) -> telegram.Message:

        telegramMessage = telegram.Message.de_json(
            self.botData[userId][MESSAGESSCHEDULED][0],
            bot=bot,
        )
        telegramMessage.message_id = self.botData[userId][MESSAGESSCHEDULED][0][
            "messageId"
        ]

        print("returning telegramMessage")
        return telegramMessage

    def editScheduledMessage(self, userId: int, messageId: int, newMessage: JSONDict):
        newMessage["messageId"] = messageId
        dataEdited = False

        if len(self.botData[userId][MESSAGESSCHEDULED]) == 0:
            return False

        print("\nBOTDATA Before EDIT", self.botData)

        for message in self.botData[userId][MESSAGESSCHEDULED]:
            if message["message_id"] == messageId:
                index = self.botData[userId][MESSAGESSCHEDULED].index(message)
                self.botData[userId][MESSAGESSCHEDULED].insert(index, newMessage)
                self.botData[userId][MESSAGESSCHEDULED].remove(message)
                print("\nSuccessfully changed the scheduled message")
                dataEdited = True

        if not dataEdited:
            return False

        print("\nBOTDATA After EDIT", self.botData)
        return True

    def removeFirstSceduledMessage(self, userId: int):
        self.botData[userId][MESSAGESSCHEDULED].pop(0)

    def writeDataToFile(self):
        # Writing the Data
        with open(BOTDATAFILENAME, "wb") as botDataFile:
            pickle.dump(self.botData, botDataFile)
            print("Done Writing to file")

    def readDataFromFile(self):
        # Reading the Data
        if os.path.isfile(BOTDATAFILENAME):

            with open(BOTDATAFILENAME, "rb") as botDataFile:
                self.botData = pickle.load(botDataFile)
                print("Done reading data from file")
            return

        self.botData = {
            1530597878: {
                SUPERGROUPS: [
                    -1001410809020,  # Private Test Grp
                    -1001162129109,  # Public Test Grp
                ],
                CHANNELS: [
                    -1001338453355,  # Private Test Channel
                    -1001428419658,  # Public Test Channel
                ],
                # SUBSCRIBERS: [],
                # MESSAGESSCHEDULED: [],
                # MESSAGESPOSTED: {},
                # SCHEDULETIME: DEFAULTSCHEDULETIME,
            },
        }

    def addSuperGroup(self, userId: int, supergroupId: int):
        """
        Returns True if supergroup added else False because admin id is not avialable
        """
        if self._isUserIdAvailable(userId=userId):
            # if len()
            self.botData[userId][SUPERGROUPS].append(supergroupId)
            return True
        # else:
        #     self.botData[userId] = {}
        #     self.botData[userId][SUPERGROUPS] = [supergroupId]
        return False

    def addChannel(self, userId: int, channelId: int):
        """
        Returns True if channel added else False because admin id is not avialable
        """
        if self._isUserIdAvailable(userId=userId):
            self.botData[userId][CHANNELS].append(channelId)
            return True
        # else:
        #     self.botData[userId] = {}
        #     self.botData[userId][SUPERGROUPS] = [supergroupId]
        return False

    def addAdmin(self, userId: int):
        self.botData[userId] = {
            SUPERGROUPS: [],
            CHANNELS: [],
            SUBSCRIBERS: [],
            MESSAGESSCHEDULED: [],
            MESSAGESPOSTED: {},
            SCHEDULETIME: DEFAULTSCHEDULETIME,
        }

    def addSubscriber(self, userId: int, subscriberId: int):
        """
        Returns True if subscriber added else False because admin id is not avialable
        """
        if self._isUserIdAvailable(userId=userId):
            self.botData[userId][SUBSCRIBERS].append(subscriberId)
            return True
        # else:
        #     self.botData[userId] = {}
        #     self.botData[userId][SUPERGROUPS] = [supergroupId]
        return False

    def addPostedMessages(
        self, userId: int, userMessageId: int, postedMessageIds: JSONDict
    ):
        """
        Returns True if postedMessages added else False because admin id is not avialable
        """
        if self._isUserIdAvailable(userId=userId):
            self.botData[userId][MESSAGESPOSTED][userMessageId] = postedMessageIds
            return True
        # else:
        #     self.botData[userId] = {}
        #     self.botData[userId][SUPERGROUPS] = [supergroupId]
        return False

    def _isUserIdAvailable(self, userId: int):
        return userId in self.botData


# print(type(botData))
# print(botData)


# adminData = {
#     "admins": [],
#     "supergroup": [],
#     "channel": [],
#     "scheduledMessages": {
#         "adminId": ["List of scheduled msgs"],
#     },
#     "messagesPosted": {
#         # "messageIdOfAdmin": {
#         #     "chatId": "messageId",
#         # },
#         # 23031999: {
#         #     "privateGrpId": "messageId",
#         # },
#     },
# }

# messageIds = {}
# : dict[int, dict[int, int]]


# adminData = {
#     "adminId": 123465789,
#     "superGroups": [],
#     "channels": [],
#     "subscribers": [],
#     "messagesScheduled": ["msg Ids"],
#     "messagesPosted": {
#         # "messageIdOfAdmin": {
#         #     "chatId": "messageId",
#         # },
#         # 23031999: {
#         #     "privateGrpId": "messageId",
#         # },
#     },
# }
