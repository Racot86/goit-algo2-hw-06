import requests
import re

def download_text(source_url: str) -> str:
    try:
        response = requests.get(source_url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error downloading text: {e}")
        return ""


def preprocess_text(input_text: str) -> str:
    cleaned_text = re.sub(r'<.*?>', '', input_text)
    final_text = re.sub(r'[^\w\s]', '', cleaned_text.lower())
    return final_text