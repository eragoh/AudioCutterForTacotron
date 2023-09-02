from download_video import download_video
from convert_to_wav import convert_to_wav
from divider import divide
from wav_to_txt import convert

url = input('Podaj youtube url: ')
name = download_video(url)
name = convert_to_wav(name)
dir_path = divide(name)
convert(dir_path)