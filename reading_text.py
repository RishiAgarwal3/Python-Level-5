import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/Cellar/tesseract/5.5.1/bin/tesseract"

img = cv2.imread("Screenshot 2025-07-31 at 7.10.59 PM.png")
h,w,_ = img.shape
boxes = pytesseract.image_to_boxes((img))
print (boxes)
for b in boxes.splitlines():
    b = b.split(" ")
    print(b)
    if b[0] == 'a':
        x1, y1, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x1, h - y1), (x2, h - y2), (0, 255, 0), 2)
cv2.imshow("result",img)
print(pytesseract.image_to_string(img))
cv2.waitKey(0)
