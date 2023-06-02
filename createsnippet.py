import json
from pydub import AudioSegment
from datetime import datetime
from info import nm

today = datetime.today().strftime('%m-%d')
name = nm
t1 = 0
t2 = 176
b = t1 * 1000
e = t2 * 1000
output_audio = AudioSegment.from_file("savedaudiofiles/Meeting1:05-29.wav")
output_audio = output_audio[b:e]
output_audio.export(f"./savedaudiofiles/{name}-missed-meeting:{today}-.wav", format="wav", bitrate="1411k", codec="pcm_s16le")