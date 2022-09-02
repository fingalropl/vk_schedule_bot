import requests
import os
from PIL import Image
import vk_api
from dotenv import load_dotenv


load_dotenv()

GROUP_ID = os.getenv('GROUP_ID')
ALBUM_ID = os.getenv('ALBUM_ID')
MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

def get_new_image():
    try:
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    except: 
        raise Exception('Сломался API собачек')
    response = response.json()
    random_cat = response[0].get('url')
    new_resp = requests.get(random_cat, stream=True).raw
    img = Image.open(new_resp)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save('sid.jpg', 'jpeg')

def prepare_img():
    login, password = MY_EMAIL, MY_PASSWORD
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)

    get_new_image()
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        'sid.jpg',
        album_id=ALBUM_ID,
        group_id=GROUP_ID
    )

    vk_photo_url = 'photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )
    return vk_photo_url
