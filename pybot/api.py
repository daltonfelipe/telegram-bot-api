import requests
import json
from pprint import pprint


class Bot():

    api_url = 'https://api.telegram.org/bot'
    commands_list = []

    def __init__(self, api_key):
        self.api_key = api_key

    
    def get_me(self):
        return requests.get(self.api_url+self.api_key+'/getMe').json()
    
    # retorna as atualizacoes das ultimas 24 horas
    def get_updates(self):
        return requests.get(self.api_url+self.api_key+'/getUpdates').json()

    # retorna a ultima atualizacao
    def get_last_update(self):
        return self.get_updates().get('result')[-1]

    # retorna a ultima mensagem da ultima atualizacao
    def get_last_msg(self, update):
        return [
            update.get('message').get('text'),
            str(update.get('message').get('chat').get('id')),
            str(update.get('message').get('date'))
            ]

    def has_update(self):
        if len(self.get_updates().get('result')) > 0:
            return True
        return False


    def is_new_msg(self, last_msg, current_msg):
        if last_msg != current_msg:
            self.last_msg = current_msg
            return True
        return False


    def listen(self):
        last_msg = None, None
        while True:
            if self.has_update():
                last_update = self.get_last_update()
                current_msg = self.get_last_msg(last_update)

                if self.is_new_msg(last_msg, current_msg):
                    last_msg = current_msg
                    # executa o comando salvo
                    for command in self.commands_list:
                        if current_msg[0] in command:
                            command[1](Bot(self.api_key), last_update, self.get_me())
                pprint(last_msg)
            else:
                print('Sem atualizacoes')
    
    # envia uma mensagem
    def reply_text(self, text, chat_id):
        requests.get(self.api_url+self.api_key+'/sendMessage?text='+text+'&chat_id='+str(chat_id))


    def add_new_command(self, command, msg):
        self.commands_list.append([command, msg])
