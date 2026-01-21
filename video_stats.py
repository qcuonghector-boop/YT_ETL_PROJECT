import requests
import json

import os
from dotenv import load_dotenv


load_dotenv(dotenv_path = "./.env")

api_key = os.getenv("api_key")

channel_handle = 'MrBeast'


def get_playlist_id():
    
    try:
        
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={api_key}"

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        # print(json.dumps(data, indent = 4))

        channel_items = data["items"][0]

        channel_playlistid = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        # print(channel_playlistid)

        return channel_playlistid

    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__": 
    # __name__ la built_in variable cua python, value duoc xac dinh tuy thuoc vao script
    # __main__ la value cua __name__ khi script duoc chay truc tiep, khong phai import 
    # script hien tai chinh la vi du, tao function o tren, call ngay o duoi de test co chay duoc hay khong
    # khi bam Run Script, content cua __name__ duoc set thanh __main__, dieu kien duoc thoa man -> call script
    get_playlist_id()
