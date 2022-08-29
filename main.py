from email import message
import os
from dotenv import load_dotenv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')

vk_session = vk_api.VkApi(token=VK_TOKEN)
api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def send_msg(id, text):
    api.messages.send(user_id = id, message = text, random_id = 0)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        id = event.user_id

        if msg == 'привет':
            send_msg(id, 'Дарова')
