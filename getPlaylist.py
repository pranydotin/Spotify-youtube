from accessToken import getSpotifyAccessToken
from getSongs import getPlaylistData
import requests
import pandas as pd
import re

access_token = getSpotifyAccessToken()

url = "https://api.spotify.com/v1/me/playlists"

payload = {}
headers = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.request("GET", url, headers=headers, data=payload)

response = response.json()

playlist_details = [
    {"Playlist_Name": item["name"], "Playlist_ID": item["id"]}
    for item in response["items"]
]

playlist_data = pd.DataFrame(playlist_details)

# print(df)

# getting songs


output_file = "./playlists/playlists.xlsx"

with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    for index, (i, row) in enumerate(playlist_data.iterrows()):
        playlist_ID = row['Playlist_ID']
        playlist_Name = re.sub(r"[\[\]\*\/\\\?\:]", "", row['Playlist_Name'])

        url = f"https://api.spotify.com/v1/playlists/{playlist_ID}/tracks"

        df = getPlaylistData(url, [], 1)

        df.to_excel(writer, sheet_name=playlist_Name[:31], index=False)

        song_details = []
