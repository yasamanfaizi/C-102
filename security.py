import cv2
import dropbox
import time
import random
start = time.time()
def takepicture():
    img = cv2.VideoCapture(0)
    active = True
    num = random.randint(0,100)
    while(active):
        ret, frame = img.read()
        imgname = "img"+str(num)+".png"
        cv2.imwrite(imgname, frame)
        start = time.time()
        active = False
    print("Picture taken.")
    return imgname
    img.release()
    cv2.destroyAllWindows()

def upload(imgname):
    dbx = dropbox.Dropbox("s9Tlasi87tAAAAAAAAAAAQyJABoATyQYdWm6Aa6H-1qFch4h4db4yBMXDz7ZEBqs")
    with open(imgname, 'rb') as f:
        dbx.files_upload(f.read(), "/"+imgname)
        print("Image has been uploaded")

while(True):
    if((time.time()-start)>=5):
        name = takepicture()
        upload(name)