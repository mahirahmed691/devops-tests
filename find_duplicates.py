import os
import subprocess

# Directory containing images
image_directory = "/images"

# Create a dictionary to store perceptual hashes as keys and image filenames as values
hashes = {}

# Loop through the images directory
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_directory, filename)
        
        # Run phash.pl to get the perceptual hash
        result = subprocess.run(["/bin/phash.pl", image_path], capture_output=True, text=True)
        perceptual_hash = result.stdout.strip()
        
        # Check if the hash already exists in the dictionary
        if perceptual_hash in hashes:
            # Duplicate found, delete the image
            print(f"Duplicate found: {filename}")
            os.remove(image_path)
        else:
            # Add the hash to the dictionary
            hashes[perceptual_hash] = filename

