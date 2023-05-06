from line_notify import LineNotify

ACCESS_TOKEN = "nuh9EJ1J5DVBcAWmzEyOkDVqQsuRkhewzVKsqv0ZRVv"
notify = LineNotify(ACCESS_TOKEN)
notify.send("System started...")


def sendText(text):
    notify.send(text)

def sendImage(text, path):
    notify.send(text, image_path=path)


