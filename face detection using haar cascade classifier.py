import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade.xml")

img = cv.imread("Team-ManU.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# In open BGR is RGB pattern

face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 4)

for (x, y, h, w) in face_detect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)


cv.imshow("Image", img)

cv.waitKey(0)