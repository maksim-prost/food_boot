from transitions import Machine


class OrderFood():

    states = ['asleep', 'choice order food', 'payment method','confirm the selection' ]
    
    validator_messages = {
        'asleep':[],
        'choice order food': ['большую', 'маленькую'],
        'payment method':['наличными', 'картой'],
        'confirm the selection':['да'],
    }
 
    def __init__(self):
        self.params_order = {}
        self.dialog ={
            'asleep':                lambda : 'Какую вы хотите пиццу? Большую или маленькую?',
            'choice order food':     lambda : 'Как вы будете платить?',
            'payment method':        self.confirm_selection,
            'confirm the selection': lambda : 'Спасибо за заказ' if self.allowed_transition  else 'Давайте попробуем еще раз \n Напишите сообщение, чтобы оформить заказ',
        }

        self.machine = Machine(model=self, states=OrderFood.states,  initial='asleep')

        self.machine.add_transition('next', 'asleep', 'choice order food',before='return_message')
        self.machine.add_transition('next', 'choice order food', 'payment method',before='return_message', prepare='valid_msg', conditions=['transition_allowed'] )
        self.machine.add_transition('next', 'payment method','confirm the selection',before='return_message', prepare='valid_msg', conditions=['transition_allowed'])
        self.machine.add_transition('next', 'confirm the selection', 'asleep',before='return_message', prepare='valid_msg')
    
    def return_message(self, message):
        self.params_order[self.state] = message
        self.message = self.dialog[self.state]()

    def valid_msg(self, message):
        self.allowed_transition = message.lower() in OrderFood.validator_messages[self.state]

    @property
    def transition_allowed(self ):
        return self.allowed_transition

    def confirm_selection(self):
        size = self.params_order.get('choice order food')
        payment = self.params_order.get('payment method')
        return f'Вы хотите {size} пиццу, оплата - {payment}?'
