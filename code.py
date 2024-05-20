import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def compress_image(input_path, output_path, target_size=2*1024*1024):
    """Compress an image to a target size in bytes."""
    with Image.open(input_path) as img:
        img_format = img.format
        quality = 95  # Start with a high quality value
        img.save(output_path, format=img_format, quality=quality)
        
        while os.path.getsize(output_path) > target_size and quality > 10:
            quality -= 5
            img.save(output_path, format=img_format, quality=quality)

def select_folder():
    """Open a dialog to select a folder and return the path."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory()
    return folder_path

def main():
    input_folder = select_folder()
    if not input_folder:
        print("No folder selected. Exiting...")
        return
    
    output_folder = os.path.join(input_folder, 'compressed')
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            output_path = os.path.join(output_folder, filename)
            compress_image(input_path, output_path)
            print(f"Compressed {filename} and saved to {output_path}")

if __name__ == "__main__":
    main()
