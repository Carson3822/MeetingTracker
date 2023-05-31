# MeetingTracker
## Description
The MeetingApp application allows company boards and teams to keep their absent members up-to-date on all matters 
discussed during meetings that involve the missing members. All it requires is the meeting is recorded and that 
attendance is taken at the beginning of every meeting in the Applications UI.

When a team members name is mentioned, and they are not present in the meeting, a snippet of the audio/video file 
+- 2 mins before and after their name is mentioned is automatically emailed to them using the smtplib and 
Email libraries.

It works by taking a recorded video/audio file and running it through Deepgram's Speech-to-text API (S-T API). 
the API outputs a JSON file containing the transcribed audio, as well as times stamps for each word and 
accuracy-confidence. check their website for more info. (https://deepgram.com) 

the MeetingApp scrapes through the JSON file provided by the S-T API and finds when the missing members name is mentioned. it then takes the time-stamp in which they are mentioned and sends a snippet of the WAV audio file as above mentioned. this action is 
preformed for each missing team member.

Users must create a account with deepgram and set up private key for the API to work.
- if a error raises urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1049)>
- it is recommended that the user find their python interpreter application in their applications folder and double click 
"Install Certificates.command" file.

Deepgram's speech to text API was selected as it accepts over 40 common audio files (MP3, WAV, FLAC, M4A) 

## Milestones/Planned features
1. send emails with gmail
   - support for other email types
2. Deepgram API integration
   - accept prerecorded audio files
   - accept prerecorded video files
3. Allow database integration (AWS)
4. Design and develop functioning UI
5. Testing
6. Dockerize
# MeetingTracker

