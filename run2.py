import torch
import cv2

model = torch.hub.load('.', 'custom', path='best.pt', source='local') 
img = cv2.imread('./data/images/bus.jpg')

results = model(img)
print(results)
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


