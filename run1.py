import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
img_bgr = cv2.imread('./data/images/bus.jpg')

# Convert BGR to RGB by reversing the order of the channels
img_rgb = img_bgr[...,::-1]

results = model(img_rgb)
results.show()
results.print()

print(results.pandas().xyxy[0])
print(results.pandas().xyxy[0].to_json(orient="records"))

# results.show()
# print(results)
# cv2.imshow('Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




