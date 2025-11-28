import cv2
from cvzone.HandTrackingModule import HandDetector



detector = HandDetector(detectionCon=0.3 , maxHands=10)


cap=cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)


