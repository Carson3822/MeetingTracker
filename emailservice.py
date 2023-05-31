# Import smtplib for the actual sending function.
import smtplib
from email.message import EmailMessage
from datetime import datetime
from pathlib import Path
from string import Template
from info import *


# The mail addresses and password

sender_address = s_a
sender_pass = s_p
receiver_address = rec_a


# Create the container email message.
def create_MIME_msg(audio_file_path):
    curr_date = datetime.today().strftime('%m-%d')
    html = Template(Path("emailformat.html").read_text())
    msg = EmailMessage()
    msg['From'] = sender_address
    msg['To'] = receiver_address
    msg['Subject'] = f"You were mentioned in a Missed Meeting: {curr_date}"
    msg.set_content(html.substitute(name=missing_members["E01"]["fullname"]), 'html')

    # attach audio file
    with open(audio_file_path, 'rb') as fp:
        audio_data = fp.read()
    msg.add_attachment(audio_data, maintype="audio", subtype="WAV")
    fp.close()
    return msg


# send message with gmail server
def send_mail(msg):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # smtp is a protocol
        smtp.ehlo()
        smtp.starttls()  # tls is an encryption mecanism

        smtp.login(sender_address, sender_pass)  # email name, password logs us into server
        smtp.send_message(msg)
        print("Success")


if __name__ == "__main__":
    send_mail(create_MIME_msg())