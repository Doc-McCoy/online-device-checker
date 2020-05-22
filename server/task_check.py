import requests
from mongo import Mongo
from bot import Bot


def check():
    db = Mongo()
    data = db.get()
    telegram_bot = Bot()

    for client in data['clients']:
        if not is_online(client['url']):
            telegram_bot.notify(client['name'])

def is_online(url):
    complete_url = url + '/check'
    try:
        response = requests.get(complete_url)
        if response.status_code == 200:
            return True
        return False
    except:
        return False

if __name__ == "__main__":
    check()
