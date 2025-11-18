import numpy as np
from pedalboard.io import AudioFile

coef = 0.55
atraso = 200
with AudioFile("LAB-III/audios/original.wav") as f:
    audio = f.read(f.frames)[0]   # canal 0
    sr = f.samplerate
N = len(audio)
resultado = np.zeros(N)
buffer = np.zeros(atraso)
pos = 0
for n in range(N):
    x = audio[n]
    delayed = buffer[pos]
    y = x + coef * delayed
    resultado[n] = y
    buffer[pos] = y
    pos = (pos + 1) % atraso
with AudioFile("saida_comb.wav", "w", sr, 1) as f:
    f.write(resultado[np.newaxis, :])
