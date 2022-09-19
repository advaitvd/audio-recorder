#!/home/advait/anaconda3/bin/python
import pyaudio
import wave
import time
import sys
import os

def play_audio(file_name="voice.wav"):
    path = os.getcwd()+"/recordings/"+file_name

    if not os.path.isfile(path):
        print("File doesnot exist. Exiting.")
        sys.exit(1)

    wf = wave.open(path, 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (7)
    p.terminate()


if __name__=="__main__":
    play_audio()