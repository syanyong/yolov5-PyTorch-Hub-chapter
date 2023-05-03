import torch
import cv2
import numpy as np
import json

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', device='mps')
# vid = cv2.VideoCapture("rtsp://tapoadmin:kkk@10.26.6.104:554/stream1")


# https://gist.github.com/syanyong/5fd83ff7d006d4566e115f9dbf203905
def plot_boxes(classes, result_dict, frame):

    for ob in result_dict:
        rec_start = (int(ob['xmin']), int(ob['ymin']))
        rec_end = (int(ob['xmax']), int(ob['ymax']))
        color = (255, 0, 0)
        thickness = 3

        cv2.rectangle(frame, rec_start, rec_end, color, thickness)
        cv2.putText(frame, "%s %0.2f" % (ob['name'], ob['confidence']), rec_start, cv2.FONT_HERSHEY_DUPLEX, 2, color, thickness)

    return frame

while(True):
    ret, frame = vid.read()
    results = model(frame)
    result_jsons = results.pandas().xyxy[0].to_json(orient="records")
    result_dict = json.loads(result_jsons)
    cv2.imshow('YOLO', plot_boxes(model.names, result_dict, frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()


