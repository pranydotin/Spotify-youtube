import requests
import json
from accessToken import getYoutubeAccessToken


def createPlaylist(name):
    url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,status"
    access = getYoutubeAccessToken()

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
        response = response.json()

        return response['id']


# print(createPlaylist("pranay"))
