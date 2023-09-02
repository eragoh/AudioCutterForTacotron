from pydub import AudioSegment, silence
from pydub.silence import split_on_silence
import os

def divide(input_wav_file):
    sound = AudioSegment.from_wav(input_wav_file)
    output_dir = f"output_segments_{input_wav_file.split('.wav')[0]}"
    os.mkdir(output_dir)
    audio_chunks = split_on_silence(sound, min_silence_len=200, silence_thresh=-40 )
    for i, chunk in enumerate(audio_chunks):
        output_file = f"{output_dir}/f{i}.wav"
        print("Exporting file", output_file)
        chunk.export(output_file, format="wav")
    return output_dir