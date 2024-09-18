#Numpy, pytorch, pandas, librosa

#RESAMPLE ALL TRACKS AT 22.5 kHz
##ML using WAV Files: https://github.com/mostafaelaraby/wavegan-pytorch/blob/master/utils.py
#Get MAESTRO Samples using metadata!!
#DOWNLOAD DIFFERENT DATASET
import numpy as np
import torch
import pandas as pd
import librosa
from torch.utils.data import Dataset
import os


class TrainDataset(Dataset):
    def __init__(self, metadata_path):
        pass
    def __len__(self):
        pass
    def __getitem__(self, index):
        pass
    def cut_sample(self):
        '''cut the music sample to the correct length'''




    


