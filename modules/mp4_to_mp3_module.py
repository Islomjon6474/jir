import subprocess
import os

def mp3Converter(file_path):
    
    base_path, _ = os.path.splitext(file_path)
    mp3_file_path = base_path + '.mp3'
    print("modified path: ", mp3_file_path)
    try:
        # Use 'ffmpeg.exe' on Windows
        subprocess.run(['ffmpeg.exe', '-y', '-i', file_path, mp3_file_path], check=True)
        return mp3_file_path
    except subprocess.CalledProcessError:
        return None
