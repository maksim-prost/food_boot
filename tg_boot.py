from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from config import TOKEN

# получаем экземпляр `Updater`
updater = Updater(token=TOKEN)
updater.start_polling()


def telegram_dispatcher_start(order_registration):

    def connection_user(update, context):
        current_chat_id = update.effective_chat.id
        message = update.message.text
        text = order_registration(current_chat_id,message)
        context.bot.send_message(chat_id=current_chat_id,text=text)   

    connection_user_handler = MessageHandler(Filters.text & (~Filters.command), connection_user)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(connection_user_handler)
