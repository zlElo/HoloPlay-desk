import webview
import json
import os

def window():
    url_to_json = os.path.expanduser("~/Documents/HoloPlay/settings.json")

    with open(url_to_json, "r") as f:
        datas = json.load(f)
    
    holoplay_url = datas["url"]
    private_mode_setting = datas["private_mode"]

    if private_mode_setting == "0":
        private_mode_setting = False
    elif private_mode_setting == "1":
        private_mode_setting = True


    # Create a webview window
    webview.create_window('HoloPlay', url=holoplay_url)


    # Start the webview
    webview.start(private_mode=private_mode_setting)