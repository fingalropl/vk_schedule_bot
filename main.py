from cgitb import text
import os
from dotenv import load_dotenv
import vk_api
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from Apidogs import prepare_img
from schedule import get_shedule
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


def send_mes(id, text, img):
    print(img)
    if img is not True:
        api.messages.send(chat_id = id, message = text, random_id = 0)


def send_doggy(id, text):
    api.messages.send(chat_id = id, message = text, random_id = 0, attachment = prepare_img())


def send_video(id, text, vid):
    api.messages.send(chat_id = id, message = text, random_id = 0, attachment = vid)


def send_shedule(id):
    shedule_comment = get_shedule()
    text = shedule_comment['text']
    shedule = shedule_comment['img']
    api.messages.send(chat_id = id, message = text, random_id = 0, attachment = shedule)


def send_hi(id, text):
    api.messages.send(chat_id = id, message = text, random_id = 0)


def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            msg = event.object['message']['text'].lower()
            id = event.chat_id
            print(msg)
            if msg == 'собачку!':
                send_doggy(id=id, text='Бери')
            elif msg == 'ты всего лишь робот, твоя жизнь не имеет смысла!':
                send_video(id=id, text=' ', vid='video341601157_456239127')
            elif msg == 'расписание':
                send_shedule(id=id)
            elif msg == 'привет':
                send_hi(id=id, text = 'Привет. Можешь попросить расписание командой "расписание", фотку собачки - "Собачку!" еще можешь написать (лучше не надо) - "ты всего лишь робот, твоя жизнь не имеет смысла!". Отмечать меня в этих сообщениях не надо. Предложения по улучшениям пиши моему создателю "vk.com/fingalropl".')

if __name__ == '__main__':
    main()
