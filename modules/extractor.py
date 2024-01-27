from mp4_to_mp3_module import mp3Converter
from mohir_ai_api_module import mohirAI
import json

import subprocess
import os

def mp3Converter(file_path):
    mp3_file_path = mp3Converter(file_path)
    response_text = mohirAI(mp3_file_path or file_path)

    json_data = json.loads(response_text)
    print(json_data["result"]["text"])


    words = ['pul', 'mohir', 'kerak']

    # Initialize a new array for matching objects
    new_array = []

    # Extract the "offsets" array from the JSON data
    offsets = json_data["result"]["offsets"]

    # Iterate through the "offsets" array and check for matches with words
    for offset in offsets:
        word = offset["word"]
        if word in words:
            start = offset["start"]
            end = offset["end"]
            lowest_start = min(lowest_start, start)
            highest_end = max(highest_end, end)

    # Print the lowest start and highest end values
    print("Lowest Start:", lowest_start)
    print("Highest End:", highest_end)

    lowest_start -= 5000
    highest_end += 3000
    if (lowest_start < 0):
        lowest_start = 0