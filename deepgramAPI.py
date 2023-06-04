from deepgram import Deepgram
import json
from info import input_audio_filepath, YOUR_SECRET_KEY

# Insert your API key from deepgram
DEEPGRAM_API_KEY = YOUR_SECRET_KEY

# Replace with your file path and audio mimetype
PATH_TO_FILE = input_audio_filepath
MIMETYPE = 'audio/wav'


def call_api():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': MIMETYPE}
        options = {"punctuate": True, "model": "nova", "language": "en-US"}

        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process.')

        response = dg_client.transcription.sync_prerecorded(source, options)
        with open("OutputData/jsonfiles/responseapi.json", "w") as f:
            print(json.dumps(response, indent=4), file=f)

        return "./OutputData/jsonfiles/responseapi.json"
