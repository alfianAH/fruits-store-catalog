#!/usr/bin/env python3

import os
import re
import requests

# TODO: Change [linux-instance-external-IP]
url = "http://34.122.71.95/fruits/"
desc_dir = os.path.join("supplier-data", "descriptions")
text_file_name_pattern = r"([0-9]+).txt$"


def make_json_object(text_file, text_file_name):
    """Make JSON object from text file. Text file format:
    * name
    * weight (in lbs)
    * description

    :param text_file_name: Text file name without extension
    :param text_file: Files in ~/supplier-data/descriptions
    :return: JSON Dictionary
    """

    json_dict = {}
    desc_keys = ["name", "weight", "description", "image_name"]

    # Open text file
    with open(text_file, 'r') as opened_text_file:
        # Add dictionary value
        for index, sentence in enumerate(opened_text_file.readlines()):
            sentence = sentence.strip()
            # If sentence is weight:
            if index == 1:
                weight_pattern = r"([0-9]+) lbs$"
                result = re.search(weight_pattern, sentence)
                json_dict[desc_keys[index]] = int(result.groups()[0])
            else:
                json_dict[desc_keys[index]] = sentence

    # Add image_name value in dictionary
    json_dict[desc_keys[-1]] = "{}.jpeg".format(text_file_name)

    return json_dict


def upload_to_web(desc_dict):
    """POST descriptions JSON to website

    :param desc_dict: description dictionary
    :return:
    """

    # POST desc_dict to url
    req = requests.post(url, data=desc_dict)

    # Give output when the request is okay
    if req.ok:
        print("Successfully upload JSON to {}".format(url))

    # Raise error when the request is not okay
    req.raise_for_status()


def main():
    """Iterate text files in ~/supplier-data/descriptions folder"""

    # Iterate files in desc_dir
    for file in os.listdir(desc_dir):
        try:
            # Search file name in desc_dir
            result = re.search(text_file_name_pattern, file)
            text_file_name = result.groups()[0]

            # If there is the result, ...
            if result:
                file_path = os.path.join(desc_dir, file)
                # Make JSON object
                json_obj = make_json_object(file_path, text_file_name)
                # Upload json_obj to website
                upload_to_web(json_obj)
        except AttributeError:
            continue


if __name__ == '__main__':
    main()
