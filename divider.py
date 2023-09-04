from pydub import AudioSegment, silence
from pydub.silence import split_on_silence
import os

def divide(input_wav_file, output_path):
    sound = AudioSegment.from_wav(output_path + '/' + input_wav_file)
    output_dir = f"{output_path}/output_segments_{input_wav_file.split('.wav')[0]}"

    os.makedirs(output_dir, exist_ok=True)
        
    audio_chunks = split_on_silence(sound, min_silence_len=200, silence_thresh=-50 )
    i = 0
    silence_chunk = AudioSegment.silent(duration=200)

    for chunk in audio_chunks:
        if len(chunk) < 1000:
            continue
        output_file = f"{output_dir}/f{i}.wav"
        print(f"Exporting file: {output_file}, length is {len(chunk)}")
        final_chunk = silence_chunk + chunk + silence_chunk
        final_chunk.export(output_file, format="wav")
        i += 1
    return output_dir