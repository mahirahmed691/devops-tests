import os
import subprocess

# Directory containing images
image_directory = "./images"

# the path to phash.pl
phash_script = "/app/bin/phash.pl"

# Create a dictionary to store perceptual hashes as keys and image filenames as values
hashes = {}

# Looping through the images directory
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_directory, filename)

        # Running phash.pl to get the perceptual hash
        result = subprocess.run([phash_script, image_path], capture_output=True, text=True)
        perceptual_hash = result.stdout.strip()

        # Checking if the hash already exists in the dictionary
	# commentt os.remove line to remove duplicate image #
        if perceptual_hash in hashes:
            # Duplicate found, delete the image
            print(f"Duplicate found: {filename}")
            # os.remove(image_path)
        else:
            # Adding the hash to the dictionary
            hashes[perceptual_hash] = filename

