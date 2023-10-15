import os

def create_dir():
    # path to the documents folder
    documents_folder = os.path.expanduser("~/Documents")

    new_folder = "HoloPlay"

    # Pfad zum neuen Ordner
    new_folder_path = os.path.join(documents_folder, new_folder)

    # check already existing
    if not os.path.exists(new_folder_path):
        # create folder
        os.makedirs(new_folder_path)
        print("[log] created settings folder")
    else:
        print("[log] folder already exists, don't create new")
