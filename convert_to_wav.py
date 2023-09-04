import os
from moviepy.editor import VideoFileClip

def convert_to_wav(video_file_name, output_path):
    video_file_path = os.path.join(output_path, video_file_name)
    video_clip = VideoFileClip(video_file_path)
    audio = video_clip.audio
    audio_file_path = os.path.join(output_path, f"{video_file_name.split('.')[0]}.wav")
    audio.write_audiofile(audio_file_path)
    video_clip.close()
    audio.close()
    os.remove(output_path + '/' + video_file_name)
    print(f"Conversion to .wav completed. Saved as '{video_file_name.split('.')[0]}.wav'.")
    return video_file_name.replace('.mp4', '.wav')