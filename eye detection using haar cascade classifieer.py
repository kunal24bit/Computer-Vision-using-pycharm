import cv2 as cv

eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

img = cv.imread("Ronaldo-1.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
eye_detect = eye_cascade.detectMultiScale(gray_img)

for (x, y, h, w) in eye_detect:
    for (x, y, h, w) in face_detect:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)



cv.imshow("Image", img)

cv.waitKey(0)