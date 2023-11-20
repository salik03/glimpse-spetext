import os

def list_files_in_folder(folder_path):
    try:
        # Check if the provided path is a valid directory
        if os.path.isdir(folder_path):
            # Get the list of files in the folder
            files = os.listdir(folder_path)

            # Print the list of files without extensions
            print(f"Files in {folder_path} (without extensions):")
            for file in files:
                # Split the file name and extension
                file_name, file_extension = os.path.splitext(file)
                print(file_name)
        else:
            print(f"The provided path '{folder_path}' is not a valid directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_folder_path' with the path of the folder you want to list
folder_path = 'finaldataset'
list_files_in_folder(folder_path)
