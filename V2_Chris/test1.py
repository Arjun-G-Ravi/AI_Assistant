

''' THIS LISTENS TO YOU FOR 4 SEC AND DOES STT

from numpy import frombuffer, int16
from pyaudio import PyAudio,paInt16
from whisper import load_model
from warnings import filterwarnings

class STT:
    def __init__(self):
        filterwarnings('ignore')
        
    def myCommand(self): 
        chunk = 1024 
        sample_format = paInt16  
        channels = 1
        fs = 16000 
        seconds = 4
        p = PyAudio()
        model = load_model("small.en")
        stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
        frames = []
        print("Recording...")
        for _ in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        print("Recording completed.")
        
        audio_data = frombuffer(b''.join(frames), dtype=int16)
        audio_data = audio_data.astype('float32') / 32767.0
        result = model.transcribe(audio_data)
        print(result["text"])
        p.terminate()
        
        
obj = STT()
while True:
    obj.myCommand()
'''