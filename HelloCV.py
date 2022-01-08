import sys
import cv2

print("HelloCV.py", cv2.__version__)

img = cv2.imread('/Users/RENDEVOUSED/Documents/4_ComputerVision/ch01/cat.bmp')

if img is None:
    print("image load failed")
    sys.exit()

cv2.namedWindow("image")
cv2.imshow("image", img)
cv2.waitKey()    #wait key func가 없으면 영상 나타나지 않음


cv2.destroyAllWindows()


