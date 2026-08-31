import os
import shutil

folder = input("Enter folder path: ")

files = os.listdir(folder)

for file in files:
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        if extension == ".jpg" or extension == ".png":
            folder_name = "Images"

        elif extension == ".pdf" or extension == ".docx" or extension == ".txt":
            folder_name = "Documents"

        elif extension == ".mp3" or extension == ".wav":
            folder_name = "Audio"

        elif extension == ".mp4" or extension == ".mkv":
            folder_name = "Videos"

        else:
            folder_name = "Others"

        new_folder = os.path.join(folder, folder_name)

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        shutil.move(file_path, os.path.join(new_folder, file))

print("Files organized successfully.")