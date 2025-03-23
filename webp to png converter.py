from PIL import Image
import os
import time

# Define the input and output directories
input_dir = r'D:\JonSaw\Stickers\090325\Genshin 5.4'
output_dir = f"{input_dir}\\png"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a webp image (case insensitive)
    if filename.lower().endswith('.webp'):
        input_path = os.path.join(input_dir, filename)
        # Open the image using Pillow
        with Image.open(input_path) as img:
            # Resize the image to 512x512 pixels
            img_resized = img.resize((512, 512))
            # Generate the output file path with a png extension
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_dir, base_name + '.png')
            # Save the resized image in png format
            img_resized.save(output_path, 'PNG')
            
        print(f"Converted and resized: {filename} -> {base_name}.png")
