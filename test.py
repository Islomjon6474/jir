from modules.mp4_to_mp3_module import mp3Converter
from modules.mohir_ai_api_module import mohirAI
from modules.extractor import extractor
import json


file_path = "C:\\Users\\musya\\Videos\\amateur_video.mp4"
print(file_path)
hello = mohirAI(file_path)

print(hello)