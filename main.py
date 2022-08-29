import os
from dotenv import load_dotenv
import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from Apidogs import prepare_img
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')

vk_session = vk_api.VkApi(token=VK_TOKEN)
api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def get_but(text):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": "positive"
            }


def get_keyboard(text):
    return {
        'one_time' : False,
        'buttons' : [
            [get_but(text)]
        ]
    }


def json_keyboard(text):
    key = get_keyboard(text)
    keyboard = json.dumps(key, ensure_ascii = False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))  
    return keyboard

# def send_msg(id, text):
#     api.messages.send(chat_id = id, message = text, random_id = 0)

def send_mes(id, text, but_text, img):
    print(img)
    if img is not True:
        api.messages.send(chat_id = id, message = text, random_id = 0, keyboard = json_keyboard(but_text))
    else:
        api.messages.send(chat_id = id, message = text, random_id = 0, keyboard = json_keyboard(but_text), attachment = prepare_img())

def send_end_story(id, text, but_text):
    for i in range(3):
        api.messages.send(chat_id = id, message = text, random_id = 0, keyboard = json_keyboard(but_text), attachment = prepare_img())


def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_chat:
            msg = event.text.lower()
            id = event.chat_id
            print(msg)
            if msg == 'привет':
                send_mes(id = id, text ='Дарова', but_text='Может котика?', img=False)
            elif msg == '[club215622029|@public215622029] может котика?':
                send_mes(id = id, text='Котики кончились, бери собачку.',but_text = 'ОГО! Это еще лучше.', img=True)
            elif msg == '[club215622029|@public215622029] ого! это еще лучше.':
                send_mes (id = id, text='Может еще собачек?',but_text = 'Еще собачек!', img=True)
            elif msg == '[club215622029|@public215622029] еще собачек!':
                send_end_story (id = id, text='Бери, мне не жалко',but_text = 'Конец')
            elif msg == '[club215622029|учебный бот на python] может котика?':
                send_mes(id = id, text='Котики кончились, бери собачку.',but_text = 'ОГО! Это еще лучше.', img=True)
            elif msg == '[club215622029|учебный бот на python] ого! это еще лучше.':
                send_mes (id = id, text='Может еще собачек?',but_text = 'Еще собачек!', img=True)
            elif msg == '[club215622029|учебный бот на python] еще собачек!':
                send_end_story (id = id, text='Бери, мне не жалко',but_text = 'Конец')
            elif msg == '[club215622029|учебный бот на python] конец':
                send_mes (id = id, text='Конец ознакомительного отрывка бота для котиков(собачек). Ожидайте дальнейшей разработки. И кидайте донаты в группу. Чтобы начать заново, напишите "привет"',but_text = 'Может котика?', img=False)
            elif msg == '[club215622029|@public215622029] конец':
                send_mes (id = id, text='Конец ознакомительного отрывка бота для котиков(собачек). Ожидайте дальнейшей разработки. И кидайте донаты в группу. Чтобы начать заново, напишите "привет"',but_text = 'Может котика?', img=False)
            elif msg == 'привет':
                send_mes(id = id, text ='Дарова', but_text='Может котика?', img=False)
            elif msg == '[club215622029|@club215622029] может котика?':
                send_mes(id = id, text='Котики кончились, бери собачку.',but_text = 'ОГО! Это еще лучше.', img=True)
            elif msg == '[club215622029|@club215622029] ого! это еще лучше.':
                send_mes (id = id, text='Может еще собачек?',but_text = 'Еще собачек!', img=True)
            elif msg == '[club215622029|@club215622029] еще собачек!':
                send_end_story (id = id, text='Бери, мне не жалко',but_text = 'Конец')
            elif msg == '[club215622029|@club215622029] конец':
                send_mes (id = id, text='Конец ознакомительного отрывка бота для котиков(собачек). Ожидайте дальнейшей разработки. И кидайте донаты в группу. Чтобы начать заново, напишите "привет"',but_text = 'Может котика?', img=False)
if __name__ == '__main__':
    main()
