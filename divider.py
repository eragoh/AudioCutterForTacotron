from pydub import AudioSegment
import os

def divide(input_file):
    output_dir = f"output_segments_{input_file.split('.wav')[0]}"
    os.makedirs(output_dir, exist_ok=True)
    audio = AudioSegment.from_file(input_file, format="wav")
    segment_duration = 6000  # 6 seconds
    start_time = 0
    segment_number = 1
    while start_time + segment_duration <= len(audio):
        segment = audio[start_time:start_time + segment_duration]
        output_file = os.path.join(output_dir, f"segment_{segment_number}.wav")
        segment.export(output_file, format="wav")
        start_time += segment_duration
        segment_number += 1

    print(f"{segment_number - 1} segments created in '{output_dir}'")
    return output_dir