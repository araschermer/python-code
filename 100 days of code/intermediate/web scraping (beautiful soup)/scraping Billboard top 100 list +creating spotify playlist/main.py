import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

# scraping the top 100 list from Billboard
CLIENT_ID=os.environ.get("CLIENT_ID")
CLIENT_SECRET=os.environ.get("CLIENT_SECRET")
date=input("Which year do you want to travel to?"
           "Type the date in this format YYYY-MM-DD")
URL="https://www.billboard.com/charts/hot-100/"
response_text=requests.get(URL+date).text
soup = BeautifulSoup(response_text,"html.parser")
songs_names=[song_name.text  for song_name in soup.find_all("span", class_ = "chart-element__information__song text--truncate color--primary")]
singers_names=[singer_name.text for singer_name in soup.find_all("span", class_ = "chart-element__information__artist text--truncate color--secondary")]
# print(songs_names)
# print(singers_names)
songs_list=dict(zip(songs_names, singers_names))
# print(songs_list)

##-------------- Connecting to spotify API using spotipy library --------------------- ##
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope = "playlist-modify-private", redirect_uri = "http://example.com",
                                               client_id = CLIENT_ID, client_secret=CLIENT_SECRET, show_dialog=True,
                                               cache_path = "token.txt"))
user_id = sp.current_user()["id"]
# copy the url of the  example page you get redirected to  and past in in the console, when asked

year=date.split("-")[0] # getting the year from the date
songs_links=[]
for song in songs_names:
    result=sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        songs_links.append(uri)
    except IndexError:
        print(f"'{song}' does not exist on spotify")
playlist=sp.user_playlist_create(user = user_id, name=f"{date} Billboard 100", public = False)
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_links)
print(playlist['external_urls'])