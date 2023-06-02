import json
from pydub import AudioSegment
from datetime import datetime
from info import nm, filepath

today = datetime.today().strftime('%m-%d')
name = nm


def take_snippet(name: str, begin: int, end: int):
    """Takes wav audio file and outputs a snipped version at begin(sec) and end(sec)"""
    b = begin * 1000
    e = end * 1000
    output_audio = AudioSegment.from_file(filepath)
    output_audio = output_audio[b:e]
    output_audio.export(f"./savedaudiofiles/{name}-missed-meeting:{today}-.wav", format="wav", bitrate="1411k", codec="pcm_s16le")


take_snippet(nm, 0, 176)
