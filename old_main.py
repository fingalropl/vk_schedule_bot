import json
import os
from cgitb import text

import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

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

# def send_msg(id, text):
#     api.messages.send(chat_id = id, message = text, random_id = 0)

def send_mes(id, text, but_text, img):
    print(img)
    if img is not True:
        api.messages.send(chat_id = id, message = text, random_id = 0, keyboard = json_keyboard(but_text))
    # else:
    #     api.messages.send(chat_id = id, message = text, random_id = 0, keyboard = json_keyboard(but_text), attachment = prepare_img())

# def send_end_story(id, text, but_text):
#     for i in range(3):
#         api.messages.send(chat_id = id, message = text, random_id = 0, keyboard = json_keyboard(but_text), attachment = prepare_img())

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
            if msg == '????????????':
                send_mes(id = id, text ='????????????', img=False)
            # if msg == '????????????':
                # send_mes(id = id, text ='????????????', but_text='?????????? ?????????????', img=False)
            # elif msg == '[club215622029|@public215622029] ?????????? ?????????????':
                # send_mes(id = id, text='???????????? ??????????????????, ???????? ??????????????.',but_text = '??????! ?????? ?????? ??????????.', img=True)
            elif msg == '??????????????!':
                send_doggy(id=id, text='????????')
            elif msg == '???? ?????????? ???????? ??????????, ???????? ?????????? ???? ?????????? ????????????!':
                send_video(id=id, text=' ', vid='video341601157_456239127')
            elif msg == '????????????????????':
                send_shedule(id=id)
            elif msg == '[club215622029|@public215622029]':
                send_hi(id=id, text = '?? ???? ???????? ???? ?????? ????????????????. ???????????? ?????????????????? ???????????????????? ???????????????? "????????????????????", ?????????? ?????????????? - "??????????????!" ?????? ???????????? ???????????????? (?????????? ???? ????????) - "???? ?????????? ???????? ??????????, ???????? ?????????? ???? ?????????? ????????????!". ???????????????? ???????? ?? ???????? ???????????????????? ???? ????????. ?????????????????????? ???? ???????????????????? ???????? ?????????? ?????????????????? "https://vk.com/fingalropl".')
            # elif msg == '[club215622029|@public215622029] ??????! ?????? ?????? ??????????.':
            #     send_mes (id = id, text='?????????? ?????? ???????????????',but_text = '?????? ??????????????!', img=True)
            # elif msg == '[club215622029|@public215622029] ?????? ??????????????!':
            #     send_end_story (id = id, text='????????, ?????? ???? ??????????',but_text = '??????????')
            # elif msg == '[club215622029|?????????????? ?????? ???? python] ?????????? ?????????????':
            #     send_mes(id = id, text='???????????? ??????????????????, ???????? ??????????????.',but_text = '??????! ?????? ?????? ??????????.', img=True)
            # elif msg == '[club215622029|?????????????? ?????? ???? python] ??????! ?????? ?????? ??????????.':
            #     send_mes (id = id, text='?????????? ?????? ???????????????',but_text = '?????? ??????????????!', img=True)
            # elif msg == '[club215622029|?????????????? ?????? ???? python] ?????? ??????????????!':
            #     send_end_story (id = id, text='????????, ?????? ???? ??????????',but_text = '??????????')
            # elif msg == '[club215622029|?????????????? ?????? ???? python] ??????????':
            #     send_mes (id = id, text='?????????? ???????????????????????????????? ?????????????? ???????? ?????? ??????????????(??????????????). ???????????????? ???????????????????? ????????????????????. ?? ?????????????? ???????????? ?? ????????????. ?????????? ???????????? ????????????, ???????????????? "????????????"',but_text = '?????????? ?????????????', img=False)
            # elif msg == '[club215622029|@public215622029] ??????????':
            #     send_mes (id = id, text='?????????? ???????????????????????????????? ?????????????? ???????? ?????? ??????????????(??????????????). ???????????????? ???????????????????? ????????????????????. ?? ?????????????? ???????????? ?? ????????????. ?????????? ???????????? ????????????, ???????????????? "????????????"',but_text = '?????????? ?????????????', img=False)
            # elif msg == '????????????':
            #     send_mes(id = id, text ='????????????', but_text='?????????? ?????????????', img=False)
            # elif msg == '[club215622029|@club215622029] ?????????? ?????????????':
            #     send_mes(id = id, text='???????????? ??????????????????, ???????? ??????????????.',but_text = '??????! ?????? ?????? ??????????.', img=True)
            # elif msg == '[club215622029|@club215622029] ??????! ?????? ?????? ??????????.':
            #     send_mes (id = id, text='?????????? ?????? ???????????????',but_text = '?????? ??????????????!', img=True)
            # elif msg == '[club215622029|@club215622029] ?????? ??????????????!':
            #     send_end_story (id = id, text='????????, ?????? ???? ??????????',but_text = '??????????')
            # elif msg == '[club215622029|@club215622029] ??????????':
            #     send_mes (id = id, text='?????????? ???????????????????????????????? ?????????????? ???????? ?????? ??????????????(??????????????). ???????????????? ???????????????????? ????????????????????. ?? ?????????????? ???????????? ?? ????????????. ?????????? ???????????? ????????????, ???????????????? "????????????"',but_text = '?????????? ?????????????', img=False)
if __name__ == '__main__':
    main()
