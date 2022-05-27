import pyaudio
import numpy as np
import wave
import sys
# import matplotlib.pyplot as plot
# from scipy import signal
import math
from scipy.io.wavfile import write

chunk = 1024

def callback(in_data, frame_count, time_info, status):
	data1 = file1.readframes(frame_count)
	data2 = file2.readframes(frame_count)
	decodeddata1 = np.fromstring(data1, np.int16)
	decodeddata2 = np.fromstring(data2, np.int16)
	newdata = (decodeddata1 * 0.5 + decodeddata2* 0.5).astype(np.float32)
	return (result.tostring(), pyaudio.paContinue)


def play_note(file1, file2):
	p = pyaudio.PyAudio()
	volume = 0.5
	stream = p.open(format =
				p.get_format_from_width(file1.getsampwidth()),
				channels = file1.getnchannels(),
				rate = file2.getframerate(),
				output = True,
				stream_callback=callback)

	data = file1.readframes(chunk)
	while data != '':
		# writing to the stream is what *actually* plays the sound.
		stream.write(data)
		data = file1.readframes(chunk)
		# stream.write()
		# stream.stop_stream()
		# # close PyAudio (7)
	stream.close()
	p.terminate()
	
file1 = wave.open("toto.wav", 'rb')
file2 = wave.open("around.wav", 'rb')
#################

# wf = wave.open(sys.argv[1], 'rb')
play_note(file1, file2)