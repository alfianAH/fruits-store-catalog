#!/usr/bin/env python3

from PIL import Image
import re
import os

image_name_pattern = r"([0-9]+).tiff$"
images_dir = os.path.join("supplier-data", "images")


def change_image(image_file):
    """Change images' resolution and format
    * Change image resolution from 3000x2000 to 600x400 pixel
    * Change image format from .TIFF to .JPEG
    * Save converted images to ~/supplier-data/images
    """

    width, height = (600, 400)
    im = Image.open(image_file)

    # Resize and convert image from RGBA to RGB
    new_im = im.resize((width, height)).convert("RGB")

    try:
        # Search file name in image_file
        result = re.search(image_name_pattern, image_file)
        image_file_name = result.groups()[0]

        # Save new name to images_dir
        converted_image_path = os.path.join(images_dir, image_file_name)

        # Save new image in JPEG format
        new_im.save("{}.jpeg".format(converted_image_path), "JPEG")
    except AttributeError:
        pass


def main():
    """Iterate images in ~/supplier-data/images folder
    Change image
    """

    # Iterate files in images_dir
    for file in os.listdir(images_dir):
        try:
            # Search file name in image_file
            result = re.search(image_name_pattern, file)

            # If there is the result, change image
            if result:
                image_path = os.path.join(images_dir, file)
                change_image(image_path)
        except AttributeError:
            pass


if __name__ == '__main__':
    main()
