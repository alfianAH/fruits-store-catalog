#!/usr/bin/env python3

import os
import re
import requests


# TODO: Change [linux-instance-IP-Address]
url = "http://34.122.71.95/upload/"
image_name_pattern = r"([0-9]+).jpeg$"
images_dir = os.path.join("supplier-data", "images")


def upload_converted_images(image_file):
    """Upload converted images to web server"""
    with open(image_file, 'rb') as opened_image:
        req = requests.post(url, files={'file': opened_image})

        # Give output when success
        if req.ok:
            print("Successfully upload {} to {}".format(opened_image, url))

        # Raise error when POST is not successful
        req.raise_for_status()


def main():
    """Iterate JPEG images in ~/supplier-data/images folder"""

    # Iterate files in images_dir
    for file in os.listdir(images_dir):
        try:
            # Search file name in image_file
            result = re.search(image_name_pattern, file)

            # If there is the result, upload image
            if result:
                image_path = os.path.join(images_dir, file)
                upload_converted_images(image_path)
        except AttributeError:
            continue


if __name__ == '__main__':
    main()
