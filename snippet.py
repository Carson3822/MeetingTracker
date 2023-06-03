from pydub import AudioSegment
from datetime import datetime
from info import nm, filepath, em
from JSONparser import find_absent_members, find_names

team_members = {
    "E01": {"fullname": "Mark Hammond", "Email": em, "attendance": False},
    "E02": {"fullname": "Anthony Clark", "Email": em, "attendance": True},
    "E03": {"fullname": "Katie Smith", "Email": em, "attendance": False},
    "E04": {"fullname": "Tim Smith", "Email": em, "attendance": True}
}

today = datetime.today().strftime('%m-%d')
x = find_absent_members(team_members)
print(x)
print(find_names(x))
absent_info = find_names(find_absent_members(team_members))


def save_snippet(name: str, name_timestamp: float, end_timestamp: float):
    """Takes wav audio file and outputs a snipped version at begin(sec) and end(sec)"""
    # if begin - 120 not beginning of wav file, name_timestamp - 120 sec else begin = 0
    begin = (name_timestamp-120 if name_timestamp-120 > 0 else 0) * 1000
    # if name time stamp +120sec not end of wav file, name_timestamp + 120 sec else end_of_vid_timestamp (milliseconds)
    end = (name_timestamp+120 if name_timestamp+120 < end_timestamp else end_timestamp) * 1000

    print(begin, end)
    output_audio = AudioSegment.from_file(filepath)
    output_audio = output_audio[begin:end]
    output_audio.export(f"./OutputData/snippedwav/{name}-missed-meeting:{datetime.today().strftime}.wav", format="wav", bitrate="1411k", codec="pcm_s16le")


def create_snippets(compiled_data_li):
    previous_nm_ts = 0
    end_timestamp = compiled_data_li[-1]

    for i in range(len(compiled_data_li)):
        name = compiled_data_li[i][0]
        name_timestamp = compiled_data_li[i][1]
        previous_nm_ts = name_timestamp

            save_snippet(name, name_timestamp, end_timestamp)
