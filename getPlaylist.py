from accessToken import getAccessToken
import requests
import pandas as pd

access_token = getAccessToken()

url = "https://api.spotify.com/v1/me/playlists"

payload = {}
headers = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.request("GET", url, headers=headers, data=payload)

response = response.json()

playlist_details = [
    {"Playlist_Name": item["name"], "playlist_ID": item["owner"]["id"]}
    for item in response["items"]
]

df = pd.DataFrame(playlist_details)

df.to_csv("playlists.csv", index=False)
print(playlist_details)
