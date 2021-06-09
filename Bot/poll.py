from telegram import Update
from telegram.ext import CallbackContext


def poll(update: Update, context: CallbackContext):

    # if update.edited_message:
    #     print("if part")

    #     context.bot.edit_message_text(
    #         text=update.effective_message.text,
    #         chat_id=update.effective_chat.id,
    #         message_id=update.effective_message.message_id + 1,
    #         entities=update.effective_message.entities,
    #     )
    # else:
    #     print("else part")
    context.bot.send_poll(
        chat_id=update.effective_chat.id,
        # text=update.message.text,
        # disable_web_page_preview=update.message.text,
        # entities=update.message.entities,
        question=update.effective_message.poll.question,
        options=update.effective_message.poll.options,
        is_anonymous=update.effective_message.poll.is_anonymous,
        # type=update.effective_message.poll.type,  # pylint: disable=W0622
        allows_multiple_answers=update.effective_message.poll.allows_multiple_answers,
        correct_option_id=update.effective_message.poll.correct_option_id,
        is_closed=update.effective_message.poll.is_closed,
        # disable_notification=update.effective_message.poll.d,
        # reply_to_message_id=update.effective_message.reply_to,
        # reply_markup: ReplyMarkup = None,
        # timeout=update.effective_message.poll.,
        explanation=update.effective_message.poll.explanation,
        # explanation_parse_mode: ODVInput[str] = DEFAULT_NONE,
        open_period=update.effective_message.poll.open_period,
        close_date=update.effective_message.poll.close_date,
        # api_kwargs: JSONDict = None,
        # allow_sending_without_reply=update.effective_message.poll.a,
        explanation_entities=update.effective_message.poll.explanation_entities,
    )
