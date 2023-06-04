from pydub import AudioSegment
import os
from datetime import datetime
from info import input_audio_filepath, em
from JSONparser import find_absent_members, find_names

team_members = {
    "E01": {"fullname": "Mark Hammond", "Email": em, "attendance": False},
    "E02": {"fullname": "Anthony Clark", "Email": em, "attendance": True},
    "E03": {"fullname": "Katie Smith", "Email": em, "attendance": False},
    "E04": {"fullname": "Tim Smith", "Email": em, "attendance": True}
}

today = datetime.today().strftime('%m|%d')
absent_time_info = find_names(find_absent_members(team_members))


def save_snippet(name: str, begin: float, end: float, n: int):
    """Takes wav audio file and outputs a snipped version at begin(sec) and end(sec)"""
    output_audio = AudioSegment.from_file(input_audio_filepath)
    output_audio = output_audio[begin:end]
    out_file_path = f"./OutputData/snippedwav/{name}--missed-meeting-{today}--{n}.wav"
    output_audio.export(out_file_path, format="wav", bitrate="1411k", codec="pcm_s16le")


def set_timestamps(absnt_info):
    """dynamically sets length of audio snippet then saves data"""
    print(absnt_info.keys())
    for i in absnt_info.keys():
        if i != "endclip":
            print(i)
            beg_ts = (absnt_info[i][0] - 120 if absnt_info[i][0] - 120 > 0 else 0) * 1000
            end_ts = 0
            n = 0
            prev_ts = 0
            for curr_time in absnt_info[i]:
                if prev_ts == 0:
                    end_ts = (curr_time + 120 if curr_time + 120 < absnt_info["endclip"] else absnt_info["endclip"])
                    prev_ts = curr_time
                    print(prev_ts, end_ts, "1")
                elif curr_time < prev_ts + 120 < absnt_info["endclip"]:
                    end_ts = (end_ts + 10)
                    prev_ts = curr_time
                    print(prev_ts, end_ts, "2")
            print(end_ts)
            n += 1
            save_snippet(i, beg_ts * 1000, end_ts * 1000, n)


if __name__ == "__main__":
    set_timestamps(absent_time_info)