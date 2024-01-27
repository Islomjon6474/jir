from modules.mp4_to_mp3_module import mp3Converter
from modules.mohir_ai_api_module import mohirAI
from modules.words_array import words_array

import subprocess
import os
import json

def milliseconds_to_time(milliseconds):
    # Calculate hours, minutes, and seconds from milliseconds
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    # Format the time as "hh:mm:ss"
    time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    return time_format

def mp4cut(file_path, start, end):
    
    base_path, _ = os.path.splitext(file_path)
    output_file_path = base_path + '_sus.mp4'
    print("modified path: ", output_file_path)
    start_time = milliseconds_to_time(start)
    end_time = milliseconds_to_time(end)
    try:
        # Use 'ffmpeg.exe' on Windows
        subprocess.run(['ffmpeg.exe', "-ss", start_time, "-to", end_time ,'-y', '-i', file_path, output_file_path], check=True)
        return output_file_path
    except subprocess.CalledProcessError:
        return None

def extractor(file_path):
    mp3_file_path = mp3Converter(file_path)
    response_text = mohirAI(mp3_file_path)

    json_data = json.loads(response_text)

    # Initialize a new array for matching objects
    new_array = []

    # Extract the "offsets" array from the JSON data
    offsets = json_data["result"]["offsets"]

    # Initialize variables to store lowest start and highest end values
    lowest_start = float('inf')
    highest_end = 0

    # Iterate through the "offsets" array and check for matches with words
    for offset in offsets:
        word = offset["word"]
        if word in words_array:
            start = offset["start"]
            end = offset["end"]
            lowest_start = min(lowest_start, start)
            highest_end = max(highest_end, end)


    sus_line = ""
    

    lowest_start -= 5000
    highest_end += 3000
    if (lowest_start < 0):
        lowest_start = 0

    # Print the lowest start and highest end values
    print("Lowest Start:", lowest_start)
    print("Highest End:", highest_end)

    result = {
        "sus_file_path": mp4cut(file_path, int(lowest_start), int(highest_end)),
        "start": milliseconds_to_time(int(lowest_start)),
        "end": milliseconds_to_time(int(highest_end)),
        "text": json_data["result"]["text"]
    }


    return result