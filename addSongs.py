from accessToken import getYoutubeAccessToken
import pandas as pd
from handleRequest import createPlaylist
from handleRequest import searchSong
from handleRequest import insertToPlaylist

data = pd.ExcelFile("./playlists/playlists.xlsx")
# print(data.sheet_names)
# for sheet in

for sheet in data.sheet_names:
    df = data.parse(sheet)
    df = df.head(1)

    play_id = createPlaylist(sheet)
    for i, row in df.iterrows():
        print(i)
        search = f"{row.Song_Name} {row.artist_names}"
        video_id = searchSong(search)
        print(video_id)
        print(play_id)
        insertToPlaylist(play_id, video_id)
