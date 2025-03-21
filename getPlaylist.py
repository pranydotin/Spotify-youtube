from accessToken import getAccessToken

access_token=getAccessToken()

import requests

url = "https://api.spotify.com/v1/me/playlists"

payload = {}
headers = {
  'Authorization': 'Bearer BQD-IkiR7P0Hmg1jrwc_60Lz5WcRcpowMJEK8Jq_i1w_9-zEV_S4svl3uXDd4tf9HQFo-kTY9wTSDZclW4ULsgNNSUp_YpImnz8BeY3DP8C6741orSVD-Z2fiS9VTpCJD_tGKnUZb7E'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)