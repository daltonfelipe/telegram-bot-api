import api

api_key = "526775633:AAFJAmamomzJZr4WF4oZ4aBx6S8bgZ-c2w0"


bot = api.Bot(api_key)

@bot.command()
def start(handler, update, bot):
    handler.reply_text("Hello My Name is {}".format(
        bot.get('result').get('username')), 
        update.get('message').get('chat').get('id')
        )

@bot.command()
def hello(handler, update, bot):
    handler.reply_text("Hello", update.get('message').get('chat').get('id'))


@bot.command()
def teste(handler, update, bot):
    handler.reply_text("Oi", update.get('message').get('chat').get('id'))

bot.listen()