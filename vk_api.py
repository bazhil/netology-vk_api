from urllib.parse import urlencode
import  requests
from pprint import pprint

AUTH_URL='https://oauth.vk.com/authorize'
APP_ID=6348055


def authorize():
    api_auth_url = AUTH_URL
    app_id = APP_ID
    permissions = []
    # redirect_uri = 'https://oauth.vk.com/blank.html'
    # display = 'wap'
    api_version = '5.71'

    auth_url_template = '{0}?client_id={1}&scope={2}&v={5}&response_type=token'
    auth_url = auth_url_template.format(api_auth_url, app_id, api_version)

    response = requests.get(auth_url)
    pprint(response)


auth_data={
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.71'
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '9336fc591e14a161ea101257556fbba1227dd6dabd05581464751444a553b2c441cd09150285bf24a6387'
target_uid = '4401253'

def find_friends():
    params = {
        'access_token': TOKEN,
        'target_uid': target_uid
    }

    BASE_URL = 'https://api.vk.com/method/friends.getMutual'

    response = requests.get(BASE_URL, params)
    # pprint(response.json())
    # pprint(type(response.json()))
    for x, y in enumerate(response.json()['response'], 1):
        pprint(f"{x}. id друга {y}. Ссылка страницу друга: https://vk.com/id{y}")

find_friends()

authorize()