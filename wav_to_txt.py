import whisper
import os
import numpy as np
import torch

torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print('Wait until model is loaded...')
model = whisper.load_model("medium", device=DEVICE)
print(
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)

def convert_to_txt(file_name):
    print('Converting:', file_name)
    audio = whisper.load_audio(file_name)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    options = whisper.DecodingOptions(language="pl", without_timestamps=True, fp16 = False)
    result = whisper.decode(model, mel, options)
    result = model.transcribe(file_name)
    with open(file_name.replace('.wav', '.txt'), 'w') as f:
        f.write(result['text'])

def convert(dir_path):
    for f in os.listdir(dir_path):
        file_name = dir_path + '/' + f
        if not os.path.isfile(file_name):
            continue
        convert_to_txt(file_name)