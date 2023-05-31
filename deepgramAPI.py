from deepgram import Deepgram
import json
from info import filepath, YOUR_SECRET_KEY

# The API key we created in step 3
DEEPGRAM_API_KEY = YOUR_SECRET_KEY

# Replace with your file path and audio mimetype
PATH_TO_FILE = filepath
MIMETYPE = 'audio/wav'


def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': MIMETYPE}
        options = {"punctuate": True, "model": "nova", "language": "en-US"}

        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process.')
        print('While you wait, did you know that Deepgram accepts over 40 audio file formats? Even MP4s.')
        print('To learn more about customizing your transcripts check out developers.deepgram.com')

        response = dg_client.transcription.sync_prerecorded(source, options)
        return json.dumps(response, indent=4)


x = main()
