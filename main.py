from pprint import pprint

import requests

with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()


class VKUser:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_friends(self):
        response = requests.get('https://api.vk.com/method/friends.get', params={
            'access_token': token,
            'user_id': self.user_id,
            'v': '5.131'
        })

        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                return data['response']['items']
            else:
                print('Ошибка при получении списка друзей:', data)
                return []
        else:
            print('Ошибка при выполнении запроса:', response.status_code)
            return []

    def find_common_friends(self, other_user):
        self_friends = self.get_friends()
        other_friends = other_user.get_friends()
        common_friends = list(set(self_friends) & set(other_friends))
        return common_friends

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


user1 = VKUser('9134482')
user2 = VKUser('17611630')
common_friends = user1.find_common_friends(user2)
print('Общие друзья:', common_friends)

print(user1)
