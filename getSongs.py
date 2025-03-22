from accessToken import getAccessToken
from generateSongList import getPlaylistData
import requests
import pandas as pd

access_token = getAccessToken()

playlist_data = pd.read_csv("./playlists.csv")

song_details = []
global_index = 1


def getPlaylistData(url, ind):
    global global_index
    payload = {}
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
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
        getPlaylistData(next, ind)

    global_index = 1
    return pd.DataFrame(song_details)


for index, (i, row) in enumerate(playlist_data.iterrows()):
    playlist_ID = row['Playlist_ID']
    playlist_Name = row['Playlist_Name']

    url = f"https://api.spotify.com/v1/playlists/{playlist_ID}/tracks"

    df = getPlaylistData(url, index)

    song_details = []
    df.to_csv(f"{playlist_Name}.csv", index=False)
