import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Prueba Jose'
email['to'] = 'zerotomasterypythoncoursejlmv@gmail.com'
email['subject'] = 'You won a 1,000,000 dollars!'

#email.set_content('I am a Python Master')
email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomasterypythoncoursejlmv@gmail.com', 'qwerty123456$')
    smtp.send_message(email)
    print('all good boss!')
