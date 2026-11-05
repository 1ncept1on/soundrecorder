import sounddevice as sd
from scipy.io.wavfile import write
duration = int(input("Enter duration in seconds: "))
fs = 44100 
sd.default.samplerate = fs
sd.default.channels = 2
myrecording = sd.rec(int(duration * fs))
sd.wait()
write("output.wav", fs, myrecording)
