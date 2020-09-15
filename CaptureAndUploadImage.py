import cv2
import dropbox
import time
import random
startTime = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        print(ret,frame)
        imageName = 'img'+str(number)+'.png'
        print(imageName)
        cv2.imwrite(imageName,frame)
        startTime = time.time()
        result = False
    return imageName
    print('snapshotTaken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadImage(imageName):
    accessToken = 'sl.AhyFmpCRk_eYjso0IZrZ09EGuywBTXyXJuHVnx82ksQ9ScxO3bt6aemY3GxNA3jRSBvf4n3cE_cVZjuRBrq7LyeDef8ZMnwz_EX0l1mWfb4nUPqdT8JME2C9yVKDTS1onHDypFs'
    file = imageCounter
    fileFrom = file
    fileTo = '/newFolder1/'+imageName
    dbx = dropbox.Dropbox(accessToken)
    with open(fileFrom,'rb')as f:
        dbx.file_upload(f.read(),fileTo,mode = dropbox.files.WriteMode.overwrite)
        print('File Uploaded')
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name = take_snapshot()
            uploadImage(name)
main()

