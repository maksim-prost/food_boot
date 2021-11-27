from state_machine import OrderFood
from tg_boot import telegram_dispatcher_start
from test_boot import test_dispatcher_start


#на время разработки удалять параметр filename, чтобы лог выходил в консоль
import logging
logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO,
                     filename='boot_logging',
                     filemode='w'
                     )

#TODO сделать очистку от мусора
chat = {}

def order_registration(current_chat_id,message):
    order = chat.setdefault( current_chat_id, OrderFood() )
    order.next(message)
    return order.message

telegram_dispatcher_start(order_registration)
# тесты запускаются паралельно  с telegram ботом
test_dispatcher_start(order_registration)



