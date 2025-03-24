import requests
import pandas as pd


def getPlaylistData(access_token, url, song_details=[], global_index=1, playlist_name=''):
    # display fetching url
    print(f"Fetching: {url}")

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
                "index_in-playlist": global_index,
                "Song_Name": item['track']['name'],
                "Album": item['track']['album']['name'],
                "artist_names": ", ".join(artist['name']for artist in item['track']['artists']),
                "playlist_name": playlist_name
            }

        ])
        global_index += 1

    next = response.get('next')

    if next:
        getPlaylistData(access_token, next, song_details,
                        global_index, playlist_name)

    global_index = 1
    # print(song_details)
    return pd.DataFrame(song_details)
