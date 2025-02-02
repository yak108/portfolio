import os
import shutil

# Define the main folder containing cover letters
main_folder = "cover letters"

# Get all files in the directory
files = os.listdir(main_folder)

# Create a dictionary to store matches
file_pairs = {}

# Group files by base name
for file in files:
    base_name, ext = os.path.splitext(file)
    if ext in [".docx", ".pdf"]:
        if base_name not in file_pairs:
            file_pairs[base_name] = {}
        file_pairs[base_name][ext] = file

# Process matching pairs
for base_name, file_dict in file_pairs.items():
    if ".docx" in file_dict and ".pdf" in file_dict:
        new_folder_name = input(f"Enter folder name for '{file_dict['.docx']}' and '{file_dict['.pdf']}': ").strip()
        if new_folder_name:
            new_folder_path = os.path.join(main_folder, new_folder_name)
            os.makedirs(new_folder_path, exist_ok=True)

            # Move files into the new folder
            for ext in [".docx", ".pdf"]:
                old_path = os.path.join(main_folder, file_dict[ext])
                new_path = os.path.join(new_folder_path, file_dict[ext])
                shutil.move(old_path, new_path)

            print(f"Moved files to {new_folder_path}")
        else:
            print("Skipping due to empty folder name.")
