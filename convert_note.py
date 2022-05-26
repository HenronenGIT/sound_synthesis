from dataclasses import asdict
from tracemalloc import stop
import pyaudio
import numpy as np
# import matplotlib.pyplot as plot
# from scipy import signal
import math
from scipy.io.wavfile import write

def play_note(note):
    p = pyaudio.PyAudio()
    volume = 0.5
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*note)
    stream.stop_stream()
    stream.close()
    # close PyAudio (7)
    p.terminate()

def convert_note_to_hz(char):
    file = open("notes.txt", 'r')
    lines = file.readlines()
    for line in lines:
        # print(note)
        if (char in line):
            arr = line.split()
            hz = float(arr[1])
    file.close()
    return (hz)

sample_rate = 44100
duration = 0.5
freqs = []

hz = convert_note_to_hz("C5")
freqs.append(hz)
# freqs = freqs.astype(float)
print(freqs)
notes = []
### Sin waves ####
for freq in freqs:
    # note = signal.square(2 * np.pi * freq * duration)
    # note = note.astype(np.float32)
    note = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*freq/sample_rate)).astype(np.float32)
    notes.append(note)

write('test.wav', 44100, notes)
for note in notes:
    play_note(note)