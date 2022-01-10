import sys
import glob
import cv2

img_files = glob.glob("/Users/RENDEVOUSED/Documents/4_ComputerVision/ch01/images/*.jpg")

cv2.namedWindow("image", cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    cv2.imshow("image", img)

    if cv2.waitKey(1000) == 27:#esc
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()


