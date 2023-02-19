import json
import os

import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

# from Apidogs import prepare_img
from schedule import get_shedule
from text_command import COMMANDS
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

vk_session = vk_api.VkApi(token=VK_TOKEN)
api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, GROUP_ID)


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
        'one_time' : True,
        'buttons' : [
            [get_but(text)]
        ]
    }


def json_keyboard(text):
    key = get_keyboard(text)
    keyboard = json.dumps(key, ensure_ascii = False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))  
    return keyboard


def send_mes(id, text, img):
    if img is not True:
        api.messages.send(chat_id = id, message = text, random_id = 0, )


def send_video(id, text, vid):
    api.messages.send(chat_id = id, message = text, random_id = 0, attachment = vid)


#weekday - показатель дня недели; '1' - завтра, '0' - сегодня
def send_shedule(id, weekday):
    shedule, text = get_shedule(weekday)
    api.messages.send(chat_id = id, message = text, random_id = 0, attachment = shedule)


def send_text(id, text):
    api.messages.send(chat_id = id, message = text, random_id = 0)


def off_button(id, but_text):
    api.messages.send(chat_id = id, message = 'Нажмите, на кнопку "Вырубить кнопку", чтобы отключить старую кнопку.', keyboard = json_keyboard(but_text), random_id = 0)

def distributor(msg, id):
        if msg == 'расписание':
            send_shedule(id=id, weekday=0)
        elif msg == 'привет':
            send_text(id=id, text=COMMANDS['send_hi'])
        elif msg == 'расписание на завтра':
            send_shedule(id=id, weekday=1)
        elif msg == 'выключить кнопку':
            off_button(id=id, but_text = 'Вырубить кнопку.')
        elif msg=='что умеешь?' or msg=='что умеешь.' or msg=='что умеешь':
            send_text(id=id, text=COMMANDS['send_help'])
        else:
            send_text(id=id, text=COMMANDS['send_error'])

def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            msg = event.object['message']['text'].lower()
            id = event.chat_id
            try:
                name,msg = msg.split(',')
                name = name.strip(' ')
                msg = msg.strip(' ')
                print(name)
                print(msg)
                if name == 'бот':
                    distributor(msg,id)
            except:
                print(msg)


if __name__ == '__main__':
    main()
