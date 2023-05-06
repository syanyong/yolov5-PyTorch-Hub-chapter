from line_notify import LineNotify
import queue
import threading

my_queue = queue.Queue(maxsize=20)

ACCESS_TOKEN = "nuh9EJ1J5DVBcAWmzEyOkDVqQsuRkhewzVKsqv0ZRVv"
notify = LineNotify(ACCESS_TOKEN)
notify.send("System started...")


def addQueue(obj):
    if not my_queue.empty() and obj['name'] == my_queue.queue[-1]:
        return
    else:
        if my_queue.full():
            my_queue.get()
        my_queue.put(obj)

def sendText(text):
    notify.send(text)

def sendImage(text, path):
    notify.send(text, image_path=path)

def sendTextQueue(text):
    my_queue.put(text)

def threadNotify():
    result = ""
    while not my_queue.empty():
        item = my_queue.get()
        result += item + ", "
    if result != "":
        sendText(result)
    print("Notify checking...")

def startThread():
    threading.Timer(5.0, startThread).start()
    threadNotify()
    
startThread()
