import requests
import base64
import pandas as pd


def getAccessToken():
    # get the details
    data = pd.read_json("./details.json")
    refresh = data.refresh_token[0]
    client_id = data.client_id[0]
    client_secret = data.client_secret[0]

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
    return response.get('access_token')


getAccessToken()
