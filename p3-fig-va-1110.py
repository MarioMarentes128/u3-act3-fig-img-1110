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