import os

def rename_files(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Loop through each file
    for file_name in files:
        # Split the file name into words
        words = file_name.split()

        # Get the last word
        last_word = words[-1]

        # Construct the new file name
        new_file_name = os.path.join(folder_path, last_word)

        # Rename the file
        os.rename(os.path.join(folder_path, file_name), new_file_name)
        print(f"Renamed '{file_name}' to '{last_word}'")

# Replace 'path_to_your_folder' with the actual path to your folder
folder_path = 'finaldataset'
rename_files(folder_path)
