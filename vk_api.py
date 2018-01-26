from urllib.parse import urlencode
import  requests

AUTH_URL='https://oauth.vk.com/authorize'
APP_ID=6348055


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