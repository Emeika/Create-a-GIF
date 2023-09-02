import os
import imageio.v2 as imageio

# directory storing image folders
image_dir = "./images"

# directory to store the created GIFs
output_dir = "./created_gif"

# file to keep track of processed folders
processed_folders_file = "./processed_folders.txt"

def read_processed_folders(file_path):
    """Function to read the list of processed folders from the file"""
    processed_folders = set()
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            processed_folders = set(f.read().splitlines())
    return processed_folders

def write_processed_folder(file_path, folder_name):
    """Function to write a folder name to the processed folders file"""
    with open(file_path, "a") as f:
        f.write(folder_name + "\n")

# get the list of folders in the image directory
folders = [f for f in os.listdir(image_dir) if os.path.isdir(os.path.join(image_dir, f))]

# get the list of processed folders
processed_folders = read_processed_folders(processed_folders_file)

# iterate over the folders and create GIFs for new folders
for folder_name in folders:
    if folder_name not in processed_folders:
        image_files = []
        for i in range(1, 1000):
            image_file = os.path.join(image_dir, folder_name, f"{i}.png")

            # stop if no more images detected
            if os.path.isfile(image_file):
                image_files.append(image_file)
            else:
                break

        if image_files:
            # create gif
            gif = [imageio.imread(image_file) for image_file in image_files]
            output_gif_path = os.path.join(output_dir, f"{folder_name}.gif")
            imageio.mimsave(output_gif_path, gif, loop=400, duration=0.1)

            write_processed_folder(processed_folders_file, folder_name)
            print(f"Created GIF for folder: {folder_name} -> {output_gif_path}")
            
        else:
            print(f"No images found for folder: {folder_name}")

print("GIF creation process completed.")
