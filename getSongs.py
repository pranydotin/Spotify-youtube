from accessToken import getSpotifyAccessToken
import requests
import pandas as pd

access_token = getSpotifyAccessToken()

playlist_data = pd.read_csv("./playlists.csv")

song_details = []
global_index = 1


def getPlaylistData(url, song_details=[], global_index=1):
    # display fetching url
    print(f"Fetching: {url}")
    # global global_index
    payload = {}
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print status code
    print(f"response code: {response.status_code}")
    response = response.json()

    for item in response['items']:
        song_details.extend([
            {
                "index": global_index,
                "Song_Name": item['track']['name'],
                "Album": item['track']['album']['name'],
                "artist_names": ", ".join(artist['name']for artist in item['track']['artists'])
            }

        ])
        global_index += 1

    next = response.get('next')

    if next:
        getPlaylistData(next, song_details, global_index)

    global_index = 1
    return pd.DataFrame(song_details)
