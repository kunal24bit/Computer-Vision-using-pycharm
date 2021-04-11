import cv2 as cv

img = cv.imread("New_Ronaldo-1.jpg", 1)

cv.imshow("Image", img)

p = cv.waitKey()

if p == 27:
    cv.destroyAllWindows()
elif p == ord("s"):
    cv.imwrite("The-New-Ronaldo.jpg", img)
    cv.destroyAllWindows()

