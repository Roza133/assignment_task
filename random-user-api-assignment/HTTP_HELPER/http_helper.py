import requests
import json


class HttpHelper:

    @staticmethod
    def get_user_info(size=3):
        url = f'https://random-data-api.com/api/users/random_user?size={size}'
        response = requests.get(url)
        return json.dumps(response.json())
