import os
import telegram


class Bot:
    def __init__(self):
        token = os.getenv('TELEGRAM_TOKEN')
        self.channel_id = os.getenv('CHANNEL_ID', '@online_checker_doc')
        self.bot = telegram.Bot(token)

    def notify(self, name):
        message = f"> {name} está offline!"
        self.bot.send_message(
            self.channel_id,
            message
        )
