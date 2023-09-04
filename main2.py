from download_video import download_video
from convert_to_wav import convert_to_wav
from divider import divide
from wav_to_txt import convert

with open('urls.txt', 'r') as f:
    urls = str(f.read()).split('\n')

output_path = 'output_fragments'

for url in urls:
    if not url:
        continue

    name = download_video(url, output_path)
    name = convert_to_wav(name, output_path)
    dir_path = divide(name, output_path)
    convert(dir_path)