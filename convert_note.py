import pyaudio
import numpy as np
import matplotlib.pyplot as plt
# from scipy import signal
import math
from scipy.io.wavfile import write
from scipy.signal import sweep_poly
import sounddevice as sd

def play_note(note):
	p = pyaudio.PyAudio()
	volume = 0.5
	stream = p.open(format=pyaudio.paFloat32,
					channels=1,
					rate=sample_rate,
					output=True)
	# play. May repeat with different volume values (if done interactively) 
	stream.write(note)
	stream.stop_stream()
	stream.close()
	# close PyAudio (7)
	p.terminate()

def convert_note_to_hz(char):
	file = open("notes.txt", 'r')
	lines = file.readlines()
	for line in lines:
		if (char in line):
			arr = line.split()
			hz = float(arr[1])
	file.close()
	return (hz)

freqs = []
hz = convert_note_to_hz("C5")
#-------------
notes = []
duration=0.375
sample_rate=44100
chunk = 1024
#-------------

# for freq in freqs:
arr = []
note1 = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*261.63/sample_rate))
note2 = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*421/sample_rate))
note3 = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*150/sample_rate))
# note2 = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*400/sample_rate))
# test = np.arange(sample_rate)
arr = np.append(note1, note2)
arr = np.append(arr, note3)
# arr = np.append(note1, note2)
# arr = np.append(note1, note2)
print (arr)

data = arr.astype(np.float32).tobytes()
play_note(data)