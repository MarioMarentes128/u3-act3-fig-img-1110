import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

#Mario Yañez NC 1110
print("Mario Yañez Nc 1110")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_iagen = cv2.imread('casa antigua.jpg')
plt.imshow(mi_iagen)
plt.title('casa antigua y Mario Yañez 1110')
plt.show()
print("+-+-+- Puntos en la imagen +-+-+-")
plt.imshow(mi_iagen)
x = [100,100,300,230]
y = [100,400,500,480]
plt.scatter(x, y, s=20,c='red')
plt.show()
print("+-+-+- Cuadro azul en la imagen +-+-+-")
mi_iagen = cv2.imread('casa antigua.jpg')
plt.imshow(mi_iagen)
x = [150, 150, 450, 450, 150]
y = [450, 150, 150, 450, 450]
plt.plot(x, y, c = 'blue')
plt.show()
print("+-+-+- circulo verde en la imagen +-+-+-")
mi_iagen = cv2.imread('casa antigua.jpg')
plt.imshow(mi_iagen)
N = 30 # lados del poligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340,320)
r = 150 # radio
for i in range(N+1):
    t  = 2*np.pi/N+i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x, y, c='green')
plt.show()