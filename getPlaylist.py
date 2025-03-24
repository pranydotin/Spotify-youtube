from accessToken import getSpotifyAccessToken
from accessToken import generateSpotifyAccessToken
from getSongs import getPlaylistData
import requests
import pandas as pd
import re

access_token = getSpotifyAccessToken()


def sendRequest(access_token):
    url = "https://api.spotify.com/v1/me/playlists"

    payload = {}
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        response = response.json()
        playlist_details = [
            {"Playlist_Name": item["name"], "Playlist_ID": item["id"]}
            for item in response["items"]
        ]

        playlist_data = pd.DataFrame(playlist_details)

        output_file = "./playlists/playlists.xlsx"

        all_data = []

        with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
            for index, (i, row) in enumerate(playlist_data.iterrows()):
                playlist_ID = row['Playlist_ID']
                playlist_Name = row['Playlist_Name']

                url = f"https://api.spotify.com/v1/playlists/{playlist_ID}/tracks"

                df = getPlaylistData(access_token, url, [], 1, playlist_Name)
                all_data.append(df)

            final_df = pd.concat(all_data, ignore_index=True)
            final_df.to_excel(writer, index=False)

    elif response.status_code == 401:
        response = response.json()
        if response['error']['message'] == "The access token expired":
            access_token = generateSpotifyAccessToken()
            sendRequest(access_token)


sendRequest(access_token)
