import requests
from PIL import Image
from io import BytesIO

def capture_screenshot(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(filename)
