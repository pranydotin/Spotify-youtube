import requests
import json
from accessToken import getYoutubeAccessToken

access = getYoutubeAccessToken()


def createPlaylist(name):
    url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,status"
    # access = getYoutubeAccessToken()

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


def searchSong(song):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={song}"
    payload = {}
    headers = {
        'Authorization': f'Bearer {access}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    return response['items'][0]['id']['videoId']


def insertToPlaylist(playlist, video):
    url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet"

    payload = json.dumps({
        "snippet": {
            "playlistId": f"{playlist}",
            "position": 0,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": f"{video}"
            }
        }
    })
    headers = {
        'Authorization': f'Bearer {access}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
    if response.status_code == 200:
        print(f"{video} inserted")
