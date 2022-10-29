import cv2
import numpy as np

foto1 = cv2.imread("el.png",0) # Resmi gri seviye görüntü ile aldık.
cv2.imshow("Islenmemis resim .png",foto1) # Gri seviye resmi ekrana bastırdık
cv2.waitKey()

Max = np.max(foto1) # Foto1'in maksimum değere sahip olan değerini öğrendik.

#print(Max) # Max değeri bastırdık.

w,h = foto1.shape # Foto1'in kenar ve uzunluğunu bulduk.

for i in range(0, w):
    for j in range(0,h):
         indks = Max - foto1[i,j] # Max değerden sırayla bütün değerleri çıkarttık.Negatifini alıdığımız kısım.
         foto1[i,j] = indks # Çıkarttığımız sonucu resmin kendi indeksine geri yazdık.


cv2.imshow("Resmin negatifi.png",foto1) # Negatifini alıdığımız resmi bastırdık.
cv2.waitKey()
