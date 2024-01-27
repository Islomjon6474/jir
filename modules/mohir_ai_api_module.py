import requests
from config import API_KEY

def mohirAI(file_path, timeout=30):
    print("starting API call")
    url = "https://mohir.ai/api/v1/stt"
    headers = {
        "Authorization": f"{API_KEY}:16a254d5-99e0-4625-afbe-9d8564521764",
    }

    files = {
        "file": ("mohirdev.mp3", open(file_path, "rb")),
    }

    data = {
        "return_offsets": "true",
        "run_diarization": "false",
        "blocking": "true",
    }

    try:
        response = requests.post(url, headers=headers, files=files, data=data, timeout=timeout)

        if response.status_code == 200:
            print(response)
            return response.text
        else:
            return f"Request failed with status code {response.status_code}:\n{response.text}"
    except requests.exceptions.Timeout:
        return "Request timed out. The API response took too long to arrive."