import asyncio
import random
import time
import json


def test_dispatcher_start(order_registration):
    
    async def test_dialog_with_user(dialog):
        current_user_id = dialog['current_chat_id']
        for msg in dialog['list_message_user']:
            print( f"Сообщение от пользователя {current_user_id}: {msg}" )
            time.sleep( 5*random.random() )
            answer = order_registration( current_user_id, msg )
            print( f"Сообщение пользователю {current_user_id}: {answer}" )
    
    async def run_test():
        for test in list_test:
            await test_dialog_with_user(test)

    with open('list_test.json') as f:
        list_test = json.load(f)


    asyncio.run( run_test() )
