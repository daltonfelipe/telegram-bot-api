import api

api_key = "526775633:AAFJAmamomzJZr4WF4oZ4aBx6S8bgZ-c2w0"

def msg_start(handler, update, bot):
    handler.reply_text("Hello My Name is {}".format(
        bot.get('result').get('username')), 
        update.get('message').get('chat').get('id')
        )


def msg_hello(handler, update, bot):
    handler.reply_text("Hello", update.get('message').get('chat').get('id'))

bot = api.Bot(api_key)
bot.add_new_command('/start', msg_start)
bot.add_new_command('/hello', msg_hello)
bot.listen()