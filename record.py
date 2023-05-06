import pyaudio
import wave
import os

def record_audio(
    WAVE_OUTPUT_FILENAME,
    RECORD_SECONDS=5,
    CHUNK=1024,
    FORMAT=pyaudio.paInt16,
    CHANNELS=2,
    RATE=44100
):

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    path = os.getcwd()+"/recordings/"

    if not os.path.exists(path=path):
        os.makedirs(path)

    path+=WAVE_OUTPUT_FILENAME

    wf = wave.open(path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
