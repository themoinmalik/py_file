import cv2 
# Open the device at the ID 0

cap = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print("cna not open cam")

#To set the resolution

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    ret, frame = cap.read()
    cv2.imshow("preview",frame)

#Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()