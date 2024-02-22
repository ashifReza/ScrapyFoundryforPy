# import os
# import shutil

# # Function to extract foundry name from folder name
# def extract_foundry_name(folder_name):
#     return folder_name.split('-')[-1]

# # Function to move folders to appropriate directory
# def organize_folders(source_dir):
#     # Get list of all folders in the source directory
#     folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]
    
#     # Iterate through each folder
#     for folder in folders:
#         foundry_name = extract_foundry_name(folder)
        
#         # Create directory for foundry if it doesn't exist
#         foundry_dir = os.path.join(source_dir, foundry_name)
#         if not os.path.exists(foundry_dir):
#             os.makedirs(foundry_dir)
        
#         # Move folder to appropriate directory
#         source_path = os.path.join(source_dir, folder)
#         destination_path = os.path.join(foundry_dir, folder)
#         shutil.move(source_path, destination_path)
#         print(f"Moved '{folder}' to '{foundry_name}' directory")

# # Example usage:
# source_directory = "E:/scrapeTest/fonts/downloadFromFilter"
# organize_folders(source_directory)

#type 2
import os
import shutil

# Function to extract foundry name from folder name
def extract_foundry_name(folder_name):
    # Splitting folder name by 'font-' and joining words after it with space
    return ' '.join(folder_name.split('font-')[1:])

# Function to move folders to appropriate directory
def organize_folders(source_dir):
    # Get list of all folders in the source directory
    folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]
    
    # Iterate through each folder
    for folder in folders:
        foundry_name = extract_foundry_name(folder)
        
        # Create directory for foundry if it doesn't exist
        foundry_dir = os.path.join(source_dir, foundry_name)
        if not os.path.exists(foundry_dir):
            os.makedirs(foundry_dir)
        
        # Move folder to appropriate directory
        source_path = os.path.join(source_dir, folder)
        destination_path = os.path.join(foundry_dir, folder)
        shutil.move(source_path, destination_path)
        print(f"Moved '{folder}' to '{foundry_name}' directory")

# Example usage:
source_directory = "E:/scrapeTest/fonts/downloadFromFilter"
organize_folders(source_directory)
