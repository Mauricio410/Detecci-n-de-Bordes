import cv2

# Inicializar la cámara web
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame por frame
    ret, frame = cap.read()
    
    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Aplicar el detector de bordes de Canny
    edges = cv2.Canny(gray, 100, 200)
    
    # Mostrar el frame original y el frame con los bordes detectados
    cv2.imshow('Frame Original', frame)
    cv2.imshow('Bordes Detectados', edges)
    
    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()