import pandas as pd
from ytmusicapi import YTMusic, OAuthCredentials
import time
import json

ytmusic = YTMusic("browser.json")

data = pd.read_excel("./playlists/playlists.xlsx", sheet_name="Sheet15")

# print(data)
data = data[::-1]
# print(data)
# print(data.head())
playlists = pd.unique(data.playlist_index)
# print(playlists)
grouped = data.groupby('playlist_index')
# print(data)

count = 1

for playlist in playlists:
    if playlist in grouped.groups:
        for index in grouped.groups[playlist]:  # Get songs for the playlist
            row = data.loc[index]
            print(f"{row['Song_Name']}\t {row['playlist_name']}")
            song = f"{row['Song_Name']} {row['Album']}"
            search = ytmusic.search(song, filter="songs")
            # print(search)
            if count % 10 == 0:
                print("waiting")
                time.sleep(60)
            count += 1
            ytmusic.add_playlist_items(playlist, [search[0]['videoId']])
            print(row['Song_Name'])
            time.sleep(7)  # Delay per song
        print(f"playlist {playlist} added")
        time.sleep(30)
