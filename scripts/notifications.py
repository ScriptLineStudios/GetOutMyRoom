from pushbullet import Pushbullet
from scripts.config import API_KEY, VIDEO_CAPTION

def send(image):
    pb = Pushbullet(API_KEY)
    with open(image, "rb") as pic:
        file_data = pb.upload_file(pic, VIDEO_CAPTION)

    pb.push_file(**file_data)