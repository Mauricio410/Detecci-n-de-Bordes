import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Aplicar el detector de bordes de Canny
edges = cv2.Canny(image, 100, 200)

# Mostrar la imagen original y la imagen con los bordes detectados
cv2.imshow('Imagen Original', image)
cv2.imshow('Bordes Detectados', edges)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()