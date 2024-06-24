import cv2 


refwajah = cv2.CascadeClassifier("ref_wajah.xml")
kamera = cv2.VideoCapture(0)

def facedetector(frame):
    optimasi = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) 
    wajah = refwajah.detectMultiScale(optimasi, scaleFactor=2.2)
    return wajah



def faceareaframe(frame):
    for x, y, w, h, in facedetector(frame):
     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
   
def sudah():
    kamera.release()
    cv2.destroyAllWindows()
    exit()
def main():
    while True:
        _, frame = kamera.read()
        faceareaframe(frame)
        cv2.imshow("cam.ai" , frame)
        
        if cv2.waitKey(1) & 0xFF == ord('space'):
            break
if __name__ == "__main__":
    main()