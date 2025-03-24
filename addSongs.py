import pandas as pd
from createPlaylist import createPlaylist

data = pd.read_excel("./playlists/playlists.xlsx")


def sentRequestForCreatePlaylist():

    playlist_name = pd.unique(data.playlist_name)

    play_id = []

    output_file = "./playlists/playlists.xlsx"

    for playlist in playlist_name:
        youtubePlaylist_id = createPlaylist(playlist)
        play_id.append(youtubePlaylist_id)

    playlist_mapping = {name: idx for name,
                        idx in zip(playlist_name, play_id)}

    data["playlist_index"] = data["playlist_name"].map(playlist_mapping)
    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        data.to_excel(writer, index=False)


# sentRequestForCreatePlaylist()
