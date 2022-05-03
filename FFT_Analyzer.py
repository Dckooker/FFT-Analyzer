import numpy as np 
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt
import math
import time
import socket

BUFFER = 1500
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 #Hz

p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = BUFFER
)

# FFT Initial Setup
data = stream.read(BUFFER)
dataInt = struct.unpack(str(BUFFER) + 'h', data)
fft_data = np.abs(np.fft.fft(dataInt))*2/(11000*BUFFER)

# number of seconds per dance move
dance_rate = 2.0
time_since_last_dance = time.time()

hml_avg = {'H': 0, 'M': 0, 'L': 0}
last_move = True

while True:

    #send average frequency every time interval
    if time.time() - time_since_last_dance > dance_rate:
        max = ('L', 0)
        hml_avg['H'] = round(hml_avg['H']*1.7, 3)
        hml_avg['M'] = round(hml_avg['M'], 3)
        hml_avg['L'] = round(hml_avg['L'] *.35, 3)
        for x in hml_avg.items():
            max = x if x[1] > max[1] else max
        print(hml_avg)
        print(max[0])
        time_since_last_dance = time.time()
        last_move = not last_move
        hml_avg = {'H': 0, 'M': 0, 'L': 0}

    # Audio Data Input 
    data = stream.read(BUFFER)
    dataInt = struct.unpack(str(BUFFER) + 'h', data)
    fft_data = np.abs(np.fft.fft(dataInt))*2/(11000*BUFFER)

    # Frequecy Ranges
    
    highFreqs = round(np.mean( fft_data[(len(fft_data)//35):(len(fft_data)-1)//2] ),3) 

    midFreqs = round(np.mean( fft_data[(len(fft_data)//165):(len(fft_data)//40)] ),3) 

    lowFreqs = round(np.mean( fft_data[0:(len(fft_data)//185)] ),3) 

    if highFreqs >= 0.005 and highFreqs != 0.0:
        hml_avg['H'] += round(highFreqs,3)

    if midFreqs >= 0.06 and midFreqs != 0.0:
        hml_avg['M'] += round(midFreqs, 3)
        
    if lowFreqs >= 0.3 and lowFreqs != 0.0: 
        hml_avg['L'] += round(lowFreqs, 3)
