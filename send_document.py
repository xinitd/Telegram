import requests
from settings import TOKEN, recipient


def send_document(TOKEN, chat_id, file):
    url = 'https://api.telegram.org/bot{}/sendDocument'.format(TOKEN)
    data = {'chat_id': chat_id}
    document = open(file, 'rb')
    files = {'document': document}
    response = requests.post(url, data=data, files=files)
    return response


send_document(TOKEN, recipient, 'test.txt')