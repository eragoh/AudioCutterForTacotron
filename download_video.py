from pytube import YouTube
import os
import re

def clean_string(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '_', input_string)
    return cleaned_string

def download_video(url, output_path):
    os.makedirs(output_path, exist_ok=True)
    yt = YouTube(url)
    stream = yt.streams.get_lowest_resolution()
    filename = f'{clean_string(yt.title)}.mp4'
    stream.download(output_path=output_path, filename=filename)
    print(f"Download `{yt.title}` completed.")
    return filename