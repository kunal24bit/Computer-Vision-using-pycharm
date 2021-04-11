import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray_vid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", gray_vid)

    if cv.waitKey(1) & 0XFF == ord("e"):
        break

cap.release()

cv.destroyAllWindows()