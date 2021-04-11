import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade.xml")

cap = cv.VideoCapture(0)

while(cap.isOpened()):
    _, frame = cap.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    for (x, y, h, w) in face_detect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), thickness=3)

        cv.imshow("frame", frame)
    if cv.waitKey(1) & 0xFF == ord("e"):
        break
cap.release()
cv.destroyAllWindows()