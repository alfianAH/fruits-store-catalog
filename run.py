#!/usr/bin/env python3

import os
import re
import requests

# TODO: Change [linux-instance-external-IP]
url = "http://[linux-instance-external-IP]/fruits"
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


def upload_to_web():
    pass


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
                print(make_json_object(file_path, text_file_name))
        except AttributeError:
            continue


if __name__ == '__main__':
    main()