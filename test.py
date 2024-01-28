from modules.mp4_to_mp3_module import mp3Converter
from modules.mohir_ai_api_module import mohirAI
from modules.extractor import extractor
import json


file_path = "C:\\Users\\musya\\Videos\\cenis.mp4"
print(file_path)
hello = extractor(file_path)

print(hello)