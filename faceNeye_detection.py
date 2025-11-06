import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_y_end = y + h
        face_gray = gray[y:roi_y_end, x:x + w]
        face_col  = frame[y:roi_y_end, x:x + w]
        eyes = eye_cascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=8,        # higher = fewer false positives
            minSize=(20, 20)
        )

        # Keep at most 2 best eyes (largest areas)
        #eyes = sorted(eyes, key=lambda e: e[2] * e[3], reverse=True)[:2]

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_col, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)


    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
