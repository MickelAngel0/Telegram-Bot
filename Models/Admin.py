import telegram


class Admin:
    def __init__(self) -> None:
        self.chatId = None
        self.scheduledMessages: list[telegram.Message] = []
        self.postTime = 15  # seconds
        self.sentMessages: dict[int, int] = {}
