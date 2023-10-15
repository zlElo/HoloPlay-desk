import customtkinter
import os
from folder import create_dir
import json

def save_settings(url_input, privacy_check, root):
    create_dir()
    folder_save_json = os.path.expanduser("~/Documents/HoloPlay/settings.json")

    url = url_input.get()
    private_check_setting = privacy_check.get()

    datas = {
        "url": f"{url}",
        "private_mode": f"{private_check_setting}"
    }

    with open(folder_save_json, "w") as file:
        json.dump(datas, file)

    root.destroy()



def configure_window():
    root = customtkinter.CTk()
    root.title('Configuration')
    root.iconbitmap("src\logo.ico")
    root.geometry('300x200')

    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=10)

    # url settings
    url_label = customtkinter.CTkLabel(frame, text='URL:')
    url_label.pack()

    url_input = customtkinter.CTkEntry(frame)
    url_input.pack(pady=5)

    # privacy mode settings
    privacy_check = customtkinter.CTkCheckBox(frame, text='Private mode (no playlist saving!)')
    privacy_check.pack(pady=15, padx=20)

    # save settings button
    save_btn = customtkinter.CTkButton(root, text='Ok', command=lambda: save_settings(url_input, privacy_check, root))
    save_btn.pack(pady=15)

    root.mainloop()
