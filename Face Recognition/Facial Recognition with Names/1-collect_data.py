'''
Notes before you start:
1- Create a folder called 'CollectedData'.
2- Write the person's name in the name variable in the code below.
2- Inside 'CollectedData', create another folder with the person's name.
4- Repeat these steps for each individual's.
'''
import cv2 as cv
import os

path = os.getcwd()
name = 'Ahmad'
cam = cv.VideoCapture(0)
img_counter = 0

while True:
    is_success, frame = cam.read()
    if not is_success:
        print("failed to capture image.")
        break
    cv.imshow("Collecting Data by pressing space", frame)

    k = cv.waitKey(1)

    # Check if ESC is pressed
    if k % 256 == 27:
        print("ESC is pressed... Cancel")
        break

    # Check if space is pressed
    elif k % 256 == 32:
        img_name = f"{path}\CollectedData\{name}\{name}_img_{img_counter}.jpg"
        cv.imwrite(img_name, frame)
        print(img_name)
        print(f"Image #{img_counter} saved!")
        img_counter += 1

cam.release()
cv.destroyAllWindows()
