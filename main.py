import cv2
from cvzone.HandTrackingModule import HandDetector



detector = HandDetector(detectionCon=0.3 , maxHands=10)


cap=cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)


while True:
    _, img=cap.read()  # Read the frame from the camera and store it in img , ( _,) means we are ignoring the first return value
    img = cv2.flip(img, 1)
    hand,img= detector.findHands(img) # Detect hands in the image
    cv2.imshow("Image",img)  # Display the image in a window named "Image"
    cv2.waitKey(1)  #wait 1 mili second
    if cv2.waitKey(1)== ord("q"):  # If the 'q' key is pressed so remove the camera
        break
