from urllib.parse import urlencode
import  requests

AUTH_URL='https://oauth.vk.com/authorize'
APP_ID=6348055


def authorize(self):
    api_auth_url = AUTH_URL
    app_id = APP_ID
    permissions = []
    # redirect_uri = 'https://oauth.vk.com/blank.html'
    # display = 'wap'
    api_version = '5.73'

    auth_url_template = '{0}?client_id={1}&scope={2}&v={5}&response_type=token'
    auth_url = auth_url_template.format(api_auth_url, app_id, api_version)

    response = requests.get(auth_url)
    print(response)


auth_data={
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.71'
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN= '05e8d8e984b4858cdfd2ea27e6c368e6475fc9665fbd4ef298888968ef10c108e80445350de39c537ec24'

params={
    'acces_token': TOKEN,
    'user_id': 1,
    'order': 'name'
}

response= requests.get('https://api.vk.com/method/friends.getMutual', params)
print(response.json())
print(type(response.json()))