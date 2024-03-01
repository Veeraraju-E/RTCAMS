import cv2
import face_recognition
import pickle
import os

# Importing the student images into a list
folderPath = 'Images'
PathList = os.listdir(folderPath)
# print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
print(len(imgList))


# print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
print(encodeListKnown)
encodeListKnownWithIDs = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close()
print("File Saved :)")
