import numpy as np
import pandas as pd
import librosa
import os
import requests

def load_wav_file(filepath, sample_rate):
    audio, sr = librosa.load(filepath, sr=sample_rate) 
    return audio, sr

def download_audio_files(num_files):
    """This function downloads a subset of audio files from the MAESTRO V3 dataset"""
    metadata = pd.read_csv('maestro-v3.0.0.csv')
    subset_meta = metadata[metadata['split'] == 'train'].head(num_files)
    base_location = '/scratch/shareddata/dldata/maestro/v3.0.0/maestro-v3.0.0'
    
    for idx, row in subset_meta.iterrows():
        filename = row['audio_filename']
        fileurl = base_location + filename

        local_path = os.path.join('maestro_wav_files', os.path.basename(filename))

        download_file(fileurl, local_path)

def download_file(url, destination):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {destination}")
    else:
        print(f"Failed to download: {url}, {response.status_code}")

download_audio_files(10)