import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    exito, imagen = webcam.read()
    if not exito:
        break

    hands, img = rastreador.findHands(imagen)

    if hands:
        hand = hands[0]
        dedos = rastreador.fingersUp(hand)

        gesto = "Detectando..."

        if dedos == [0, 0, 0, 0, 0]:
            gesto = "MANO CERRADA"

        elif dedos == [1, 1, 1, 1, 1]:
            gesto = "MANO ABIERTA"
       
        elif dedos == [0, 1, 1, 0, 0]:
            gesto = "SIGNO DE PAZ"

        elif dedos == [1, 0, 0, 0, 0]:
            gesto = "PULGAR ARRIBA"

        cv2.putText(
            img,
            gesto,
            (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 255, 0),
            4
        )

    cv2.imshow("Gesture Control AI", img)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()
