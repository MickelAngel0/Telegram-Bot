from constants import CHANNELS, SUPER_GROUPS
import telegram


class Admin:
    def __init__(self) -> None:
        self.chatId = None
        # self.scheduledMessages: list[telegram.Message] = []

        self.scheduledImages: list[telegram.Message] = []
        self.scheduledYoutubeLinks: list[telegram.Message] = []

        self.imagePostTime = 15  # seconds
        self.textPostTime = 15  # seconds

        self.sentMessages: dict[int, dict[int, int]] = {}
        self.sendImageIfVideoListEmpty: bool = True

        self.superGroups: list[int] = []
        # self.channels: list[int] = []
        # self.subscribers: list[int] = []
