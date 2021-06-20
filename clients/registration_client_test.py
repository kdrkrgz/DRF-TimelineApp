import requests
from pprint import pprint


def client():
    credentials = {
        "username":"tastingclient",
        "email":"tasting@testing.com",
        "password1": "Testing.123",
        "password2": "Testing.123"
    }

    response = requests.post(
        url = "http://localhost:8000/api/rest-auth/registration/",
        data = credentials
    )

    print("Status Code _______ :", response.status_code)

    response_data = response.json()
    pprint(response_data)



if __name__ == '__main__':
    client()