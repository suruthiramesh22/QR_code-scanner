import cv2
import webbrowser

cap=cv2.VideoCapture(0)
detector=cv2.QRCodeDetector()
while True:
    __, img=cap.read()
    data, one, _=detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow('qrcodescanner app',img)
    if cv2.waitKey(1)==ord('q'):
        break
b=webbrowser.open(str(a))
cap.release(a)
cv2.destroyAllWindows()