import requests
from settings import TOKEN, recipient


def send_text_message(TOKEN, chat_id, message):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    response = requests.post(url, data=data)
    return response


send_text_message(TOKEN, recipient, 'Hello, world!')