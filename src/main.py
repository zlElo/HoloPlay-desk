import os
from configure_window import configure_window
from webview__window import window


folder = os.path.expanduser("~/Documents/HoloPlay")

# check if already configured on first start
if not os.path.exists(folder):
    print("[log] settings folder is not created, call configuration setup")
    configure_window()

else:
    print("[log] folder already exists, start holoplay")
    window()