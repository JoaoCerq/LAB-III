import soundfile as sf
from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile

# Lê o arquivo de áudio
with AudioFile("entrada.wav", 'r') as f:
    audio = f.read(f.frames)
    sample_rate = f.samplerate

# Cria um "board" com reverb
board = Pedalboard([
    Reverb(
        room_size=0.3,   # ~sala pequena
        dampening=0.5,
        wet_level=0.25,  # quanto de reverb
        dry_level=0.75,
        width=0.9
    )
])

# Aplica o efeito
effected = board(audio, sample_rate)

# Salva o resultado
with AudioFile("saida_reverb_room.wav", 'w', sample_rate, effected.shape[0]) as f:
    f.write(effected)
