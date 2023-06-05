from pydub import AudioSegment
from datetime import datetime
from info import input_audio_filepath, team_members, today, absent_time_info
from JSONparser import find_absent_members, find_names


def save_snippet(name: str, begin: float, end: float, n: int):
    """Takes wav audio file and outputs a snipped version at begin(sec) and end(sec)"""
    output_audio = AudioSegment.from_file(input_audio_filepath)
    output_audio = output_audio[begin:end]
    out_file_path = f"./OutputData/snippedaudio/{name}--missed-meeting-{today}--{n}.wav"
    output_audio.export(out_file_path, format="wav", bitrate="1411k", codec="pcm_s16le")


def create_snippets(absnt_info):
    """dynamically sets length of audio snippet then saves data in snippedaudio folder"""
    for i in absnt_info.keys():
        if i != "endclip":
            beg_ts = (absnt_info[i][0] - 120 if absnt_info[i][0] - 120 > 0 else 0) * 1000
            end_ts = 0
            n = 0
            prev_ts = 0
            for curr_time in absnt_info[i]:
                if prev_ts == 0:
                    end_ts = (curr_time + 120 if curr_time + 120 < absnt_info["endclip"] else absnt_info["endclip"])
                    prev_ts = curr_time
                elif curr_time < prev_ts + 120 < absnt_info["endclip"]:
                    end_ts = (end_ts + 10)
                    prev_ts = curr_time
            n += 1
            save_snippet(i.capitalize(), beg_ts * 1000, end_ts * 1000, n)


if __name__ == "__main__":
    create_snippets(absent_time_info)