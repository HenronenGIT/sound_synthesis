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

def generate_sine(a: float = 0.5, freq: float = 440.0):

	global con

	sine = a * np.sin(2.0 * np.pi * freq * 1 + con)

	# get the angle of the wave

	phase = np.angle(np.fft.fft(sine))

	# update ref var to generate subsequent sines
	# begining where the last ended

	con = phase[-1]

	return sine

sample_rate = 44100
duration = 0.5
freqs = []
hz = convert_note_to_hz("C5")
freqs.append(hz)
hz = convert_note_to_hz("C4")
freqs.append(hz)
# freqs = freqs.astype(float)
#-------------
notes = []
duration=1.5
sample_rate=44100
chunk = 1024
#-------------

### Sin waves ####
# note = []

con = 0
a = 0.5
samples = int(chunk)
t = np.arange(samples) / sample_rate
#for freq in freqs:
# note1 = np.array((np.sin(2 * np.pi * np.arange(sample_rate*duration)*400/sample_rate)).astype(np.float32))
sine = a * np.sin(2.0 * np.pi * 400 * t + con)
phase = np.angle(np.fft.fft(sine))
con = phase[-1]
note2 = np.array((np.sin(2 * np.pi * np.arange(sample_rate*duration)*600/sample_rate)).astype(np.float32))
note3 = np.array((np.sin(2 * np.pi * np.arange(sample_rate*duration)*1000/sample_rate)).astype(np.float32))
note4 = np.array((np.sin(2 * np.pi * np.arange(sample_rate*duration)*2000/sample_rate)).astype(np.float32))
note5 = np.array((np.sin(2 * np.pi * np.arange(sample_rate*duration)*1000/sample_rate)).astype(np.float32))
note6 = np.array((np.sin(2 * np.pi * np.arange(sample_rate*duration)*3000/sample_rate)).astype(np.float32))
# print(note2)
# arr = np.concatenate((note1, note2))
# arr = np.concatenate((arr, note3))
# arr = np.concatenate((arr, note4))
# arr = np.concatenate((arr, note5))
# arr = np.concatenate((arr, note6))
# print (arr)

# plt.plot(note1)
# plt.show()
#print(array)
# note = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*400/sample_rate)).astype(np.float32)
# print (note[0])
# print (note[1])


# sd.play(note)
# Compress so pyaudio can play it
# note = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*300/sample_rate))
# data = note.astype(np.float32).tostring()

# print (data2)

	# notes.append(note)
# data = note1.astype(np.float32).tostring()
# sounddevice.play(wav_wave, blocking=True)
# for note in notes:
# play_note(signal)
play_note(sine)
# play_note(note2)
# play_note(arr)