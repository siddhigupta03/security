import cv2
import time
import random
import dropbox

startTime = time.time()

def snapshot():
    numbers = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    
    while(result):
        ret,frame = videoCaptureObject.read()
        imgNames = "img"+str(numbers)+".png"
        cv2.imwrite(imgNames,frame)
        startTime = time.time()
        result = False
        return(imgNames)
    print("Image captured.")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload(imgNames):
    access_token = ""
    file = imgNames
    file_from = file
    file_to = "/test"+(imgNames)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f,file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-startTime) >= 5):
            name = snapshot()
            upload(name)

main()