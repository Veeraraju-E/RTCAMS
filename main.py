import os
import cv2
import pickle
import numpy as np
import face_recognition
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
# print(modePathList)
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
# print(len(imgModeList))

# Load the Encoding File
print("Loading Encode File")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIDs = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIDs
print(studentIds)
print("Encode File Loaded")

while True:
    success, img = cap.read()

    imgS = cv2.resize(img,(0,0),None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFace = face_recognition.face_encodings(imgS, faceCurrFrame)

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]

    for encodeFace, faceLoc in zip(encodeCurrFace,faceCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print("matches",matches)
        # print("faceDis",faceDis)

        matchIndex = np.argmin(faceDis)
        # print("Match Index",matchIndex)

        if matches[matchIndex]:
            # print("Known Face Detected")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox = 55+x1,162+y1,x2-x1,y2-y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)