from telegram import Update
from telegram.ext import CallbackContext
from Database import admin


def callbackQuery(update: Update, context: CallbackContext) -> None:
    print("Print Message")
    # print(update.effective_message)
    query = update.callback_query
    # print(query)

    # THis shows a notification
    query.answer(f"You selected {query.data}")
    # query.message.reply_to_message.message_id

    for superGrpChatId in admin.superGroups:
        result = context.bot.delete_message(
            chat_id=superGrpChatId,
            message_id=admin.sentMessages[superGrpChatId][
                query.message.reply_to_message.message_id
            ],
        )

        if result:
            query.edit_message_text(
                "Successfully Deleted",
            )
        else:
            query.edit_message_text(
                "Unable to Delete",
            )
        
        print(f'SentMsg Before Pop: {admin.sentMessages}')

        admin.sentMessages[superGrpChatId].pop(
            query.message.reply_to_message.message_id
        )
    
        print(f'SentMsg After Pop: {admin.sentMessages}')


query = {
    "id": "6573867831815447459",
    "data": "Delete",
    "chat_instance": "-353052119437232401",
    "message": {
        "new_chat_photo": [],
        "text": "Successfully Sent!\nRemaining Posts: 0",
        "reply_to_message": {
            "new_chat_photo": [],
            "text": "Test w",
            "group_chat_created": False,
            "new_chat_members": [],
            "channel_chat_created": False,
            "chat": {
                "username": "OmkarDabade",
                "last_name": "Dabade",
                "first_name": "Omkar",
                "type": "private",
                "id": 1530597878,
            },
            "entities": [],
            "message_id": 905,
            "supergroup_chat_created": False,
            "date": 1629780517,
            "delete_chat_photo": False,
            "photo": [],
            "caption_entities": [],
            "from": {
                "language_code": "en",
                "first_name": "Omkar",
                "last_name": "Dabade",
                "is_bot": False,
                "username": "OmkarDabade",
                "id": 1530597878,
            },
        },
        "reply_markup": {
            "inline_keyboard": [[{"callback_data": "Delete", "text": "Delete"}]]
        },
        "group_chat_created": False,
        "new_chat_members": [],
        "channel_chat_created": False,
        "chat": {
            "username": "OmkarDabade",
            "last_name": "Dabade",
            "first_name": "Omkar",
            "type": "private",
            "id": 1530597878,
        },
        "entities": [],
        "message_id": 908,
        "supergroup_chat_created": False,
        "date": 1629780535,
        "delete_chat_photo": False,
        "photo": [],
        "caption_entities": [],
        "from": {
            "first_name": "Omega Bot",
            "is_bot": True,
            "username": "Hitheretestbot",
            "id": 1856554532,
        },
    },
    "from": {
        "language_code": "en",
        "first_name": "Omkar",
        "last_name": "Dabade",
        "is_bot": False,
        "username": "OmkarDabade",
        "id": 1530597878,
    },
}


effctiveMsg = {
    "new_chat_photo": [],
    "message_id": 898,
    "reply_to_message": {
        "new_chat_photo": [],
        "message_id": 894,
        "text": "Test 1",
        "new_chat_members": [],
        "channel_chat_created": False,
        "date": 1629780113,
        "entities": [],
        "chat": {
            "type": "private",
            "first_name": "Omkar",
            "username": "OmkarDabade",
            "last_name": "Dabade",
            "id": 1530597878,
        },
        "photo": [],
        "delete_chat_photo": False,
        "supergroup_chat_created": False,
        "group_chat_created": False,
        "caption_entities": [],
        "from": {
            "language_code": "en",
            "username": "OmkarDabade",
            "first_name": "Omkar",
            "is_bot": False,
            "last_name": "Dabade",
            "id": 1530597878,
        },
    },
    "text": "Successfully Sent!\nRemaining Posts: 1",
    "new_chat_members": [],
    "channel_chat_created": False,
    "date": 1629780119,
    "entities": [],
    "chat": {
        "type": "private",
        "first_name": "Omkar",
        "username": "OmkarDabade",
        "last_name": "Dabade",
        "id": 1530597878,
    },
    "photo": [],
    "delete_chat_photo": False,
    "supergroup_chat_created": False,
    "reply_markup": {
        "inline_keyboard": [[{"text": "Delete", "callback_data": "Delete"}]]
    },
    "group_chat_created": False,
    "caption_entities": [],
    "from": {
        "username": "Hitheretestbot",
        "first_name": "Omega Bot",
        "is_bot": True,
        "id": 1856554532,
    },
}
