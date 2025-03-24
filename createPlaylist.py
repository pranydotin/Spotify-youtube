import requests
import json
from accessToken import getYoutubeAccessToken
from accessToken import generateYoutubeAccessToken


def createPlaylist(name):
    access = getYoutubeAccessToken()
    return sentRequest(name, access)

# print(createPlaylist("pranay"))


def sentRequest(name, access):
    url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,status"
    payload = json.dumps({
        "snippet": {
            "title": f"{name}",
            "description": "Created from Spotify Playlists",
            "tags": [
                f"{name}",
                "API call"
            ],
            "defaultLanguage": "en"
        },
        "status": {
            "privacyStatus": "private"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Playist created")
        # print(response.text)
        response = response.json()
        return response['id']

    elif response.status_code == 401:
        access = generateYoutubeAccessToken()
        print("d")
        return sentRequest(name, access)
