#!/usr/bin/env python3
import sys
import pyaudio
import numpy as np
import json
#import math
#from pyaudio import PyAudio
from scipy.io.wavfile import write
import time

sample_rate = 44100
freqs = []
freqs2 = []

def group(n, items):
	ns = [iter(items)] * n
	while True:
		yield [next(a) for a in ns]

def play_track(track, stream):
	# p = pyaudio.PyAudio()
	# stream = p.open(format=pyaudio.paFloat32,
	# 				channels=1,
	# 				rate=sample_rate,
	# 				output=True)
	# play. May repeat with different volume values (if done interactively) 
	stream.write(track)
	# stream.stop_stream()
	# stream.close()
	# # close PyAudio (7)
	# p.terminate()

def convert_note_to_hz(char):
	file = open("notes.txt", 'r')
	hz = 0
	lines = file.readlines()
	for line in lines:
		if (char in line):
			arr = line.split()
			hz = float(arr[1])
	file.close()
	return (hz)

def generate_notes(times, freqs, total_tracks, notes):
	tracks = []
	i = 0
	j = 0
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paFloat32,
					channels=1,
					rate=sample_rate,
					output=True)
	# for track in freqs:
	# 	for time in times:
	# 		for sec in time:
	# 			for hz in track:
	while (j < total_tracks):
		track = []
		i = 0
		while i < notes[j]["total"]:
			# print(freqs[j][i])
			# print(times[j][i])
			note = (np.sin(2 * np.pi * np.arange(sample_rate*times[j][i])*freqs[j][i]/sample_rate))
			track = np.append(track, note)
			i += 1
		print (track)
		tracks += [track]
		j += 1
	# print (tracks)
	data = tracks[1].astype(np.float32).tobytes()
	play_track(data, stream)
	stream.stop_stream()
	stream.close()
	p.terminate()

def music_create(tracks, total_tracks):
	durations_total = []
	freqs_total = []
	i = 0
	while i < total_tracks:
		freqs = []
		duration = []
		j = 0
		while j < tracks[i]["total"]:
			hz = convert_note_to_hz(tracks[i]["pitch"][j])
			# print(hz)
			freqs.append(hz)
			time = tracks[i]["duration"][j]
			duration.append(time)
			j += 1
		i += 1
		durations_total += [duration]
		freqs_total += [freqs]
	generate_notes(durations_total, freqs_total, total_tracks, tracks)

def collect_info(f):
	lines = f.readlines()
	tempo_word = 'tempo'
	tracks_word = 'tracks'
	i = 0
	count = 0
	track2 = dict()
	total_tracks = 0
	for line in lines:
		if tempo_word in line:
			for word in line.split():
				if word.isdigit():
					tempo = int(word)
		if tracks_word in line:
			tracks = line.split(' ')[1]
			tracks = tracks.replace("\n", "")
			tracks = tracks.split(',')
		total_count = 0
		if line[0].isdigit():
			# dynamicaly creates dictionary to store tracks in
			track2[count] = {"nbr": 0, "tracks": "", "pitch": [], "duration": [], "total": 0}
			
			# collecting nbr of track
			track2[count].update(nbr=int(line.split(':')[0]))
			#print(track2[count]["nbr"])
			track2[count].update(tracks=tracks[track2[count]["nbr"] - 1])

			# collect pitch, alteration, octave and duration
			strstr = line.replace('\n', '')
			strstr = strstr.replace('|', '')
			string = strstr.split(' ')
			string.pop(0)
			prev = 60 / tempo
			prev_octave = 4
			total_tracks += 1
			for word in string:
				j = 0
				octave_found = 0
				alter_found = 0
				stage = 0
				while j < len(word):
					if j == 0:
						total_count += 1
					# collecting pitch
					s = ''
					while j < len(word) and word[j] != '/':
						if j == 0:
							s += word[j].upper()
						else:
							s += word[j]
						j += 1
					if (len(s) == 1):
						s += '4'
					track2[count]["pitch"].append(s)
					
					# collecting duration
					if j == len(word):
						track2[count]["duration"].append(prev)
					elif word[j] == '/':
						s = ''
						j += 1
						while j < len(word):
							s += word[j]
							j += 1
						track2[count]["duration"].append(float(s))
						prev = float(s)
					j += 1
			track2[count].update(total=total_count)
			count += 1
		i += 1
	# print(json.dumps(track2, sort_keys=False, indent=1))
	music_create(track2, total_tracks)

def main(argv, argc):
	if argc == 2:
		f = open(argv[1], "r")
		collect_info(f)
	else:
		print("Usage: ./minisynth /path/to/file")

if __name__ == "__main__":
	main(sys.argv, len(sys.argv))

#pg.mixer.quit()
#pg.quit()