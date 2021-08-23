from constants import (
    ADMIN_DATA_FILENAME,
    SCHEDULED_IMAGES,
    SCHEDULED_TEXT,
    SENT_MESSAGES,
    SUPER_GROUPS,
)
import telegram
import pickle
import os
import json
from Bot import updater


class Admin:
    def __init__(self) -> None:
        self.readFromFile()

    def writeToFile(self):
        self._db: dict = {
            SENT_MESSAGES: self.sentMessages,
            SCHEDULED_IMAGES: [msg.to_dict() for msg in self.scheduledImages],
            SCHEDULED_TEXT: [msg.to_dict() for msg in self.scheduledYoutubeLinks],
            "chatId": self.chatId,
            SUPER_GROUPS: list(self.superGroups),
            "sendImageIfVideoListEmpty": self.sendImageIfVideoListEmpty,
        }

        # Writing the Data
        with open(ADMIN_DATA_FILENAME, "wb") as dataFile:
            pickle.dump(json.dumps(self._db), dataFile)
            print("Done Writing to file")

    def readFromFile(self):
        # Reading the Data
        # print("PATH: ", os.path)

        if os.path.isfile(ADMIN_DATA_FILENAME):

            with open(ADMIN_DATA_FILENAME, "rb") as dataFile:
                self._db = {}
                self._db = json.loads(pickle.load(dataFile))
                print("Done reading data from file")

                print(self._db)

            self.chatId = self._db["chatId"]
            self.scheduledImages = [
                telegram.Message.de_json(msg, bot=updater.bot)
                for msg in self._db[SCHEDULED_IMAGES]
            ]
            self.scheduledYoutubeLinks = [
                telegram.Message.de_json(msg, bot=updater.bot)
                for msg in self._db[SCHEDULED_TEXT]
            ]

            self.sentMessages = self._db[SENT_MESSAGES]
            self.sendImageIfVideoListEmpty = self._db["sendImageIfVideoListEmpty"]
            self.superGroups = set(self._db[SUPER_GROUPS])

            print(self.sentMessages, type(self.sentMessages))
            # print(self.superGroups)

            print("File read successfully")
            return

        # 132465798
        self.chatId = None

        # [Message,Message]
        self.scheduledImages: list[telegram.Message] = []
        # [Message,Message]
        self.scheduledYoutubeLinks: list[telegram.Message] = []

        # {"-10013246578" : {123 : 465, 1324 : 465}}
        self.sentMessages: dict[str, dict[str, int]] = {}
        # True | False
        self.sendImageIfVideoListEmpty: bool = True

        # [-10078946512, -10045678913]
        self.superGroups: set[int] = set()
        self.superGroups.add(-1001410809020)
        self.sentMessages[str(-1001410809020)] = {}
