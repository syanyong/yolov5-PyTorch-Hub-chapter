import torch
import cv2
import numpy as np
import json
import line

# vid = cv2.VideoCapture(0)
model = torch.hub.load('.', 'custom', path='yolov5s.pt', source='local', device='mps') 
vid = cv2.VideoCapture("rtsp://admin:Otmadmin1234@10.10.9.115:554/cam/realmonitor?channel=1&subtype=0")

# https://gist.github.com/syanyong/5fd83ff7d006d4566e115f9dbf203905
def plot_boxes(result_dict, frame):
    for ob in result_dict:
        rec_start = (int(ob['xmin']), int(ob['ymin']))
        rec_end = (int(ob['xmax']), int(ob['ymax']))
        color = (255, 0, 0)
        thickness = 3

        if ob['name'] == 'person':
            color = (0, 0, 255)
            cv2.imwrite("./output.jpg", frame)
            line.sendImage("alert", "./output.jpg")
        cv2.rectangle(frame, rec_start, rec_end, color, thickness)
        cv2.putText(frame, "%s %0.2f" % (ob['name'], ob['confidence']), rec_start, cv2.FONT_HERSHEY_DUPLEX, 2, color, thickness)
    return frame

while(True):
    ret, frame = vid.read()
    results = model(frame)
    result_jsons = results.pandas().xyxy[0].to_json(orient="records")
    result_dict = json.loads(result_jsons)
    # print(result_dict)
    frame2 = plot_boxes(result_dict, frame)
    cv2.imshow('YOLO', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
