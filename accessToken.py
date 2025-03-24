import requests
import base64
import pandas as pd


def getSpotifyAccessToken():
    data = pd.read_json("./details.json")
    return data.spotify.get("access_token")


def generateSpotifyAccessToken():
    # get the details
    data = pd.read_json("./details.json")
    refresh = data.spotify.refresh_token
    client_id = data.spotify.client_id
    client_secret = data.spotify.client_secret

    credentials = base64.b64encode(
        f"{client_id}:{client_secret}".encode()).decode()

    url = "https://accounts.spotify.com/api/token"

    payload = f'grant_type=refresh_token&refresh_token={refresh}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {credentials}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response = response.json()
    data.loc["access_token", 'spotify'] = response.get('access_token')
    data.to_json("details.json", indent=4)

    return response.get('access_token')


def getYoutubeAccessToken():
    data = pd.read_json("./details.json")
    return data.youtube.get("access_token")


def generateYoutubeAccessToken():
    data = pd.read_json("./details.json")
    refresh = data.youtube.refresh_token
    client_id = data.youtube.client_id
    client_secret = data.youtube.client_secret

    url = "https://oauth2.googleapis.com/token"

    payload = f'client_id={client_id}&client_secret={client_secret}&redirect_uri=https%3A%2F%2Fwww.example.com&grant_type=refresh_token&refresh_token={refresh}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    data.loc["access_token", 'youtube'] = response.get('access_token')
    data.to_json("details.json", indent=4)
    return response.get('access_token')


# a = generateSpotifyAccessToken()
# print(a)
# a = getYoutubeAccessToken()
# print(a)
