import cv2
import numpy as np

#BU KISIMDA RESMİN RENKLİ HALİNİ OKUYUP BASTIRDIK.
renkli = cv2.imread("goruntu isleme resmi.png") # Resmin renkli halini dosyadan okumak.
cv2.imshow("goruntu isleme resmi yeni .png",renkli) # Resmin rekli halini ekrana bastırmak.


#BU KISIMDA RESMİ GRİ SEVİYE GÖRÜNTÜ OLARAK ALDIK.
foto = cv2.imread("goruntu isleme resmi.png",0) # Resmi gri seviye görüntü ile almak.
cv2.imshow("goruntu isleme resmi yeni .png",foto) # Gri görüntü halini ekrana bastırmak.
cv2.waitKey()

histSize = 256  # Histogram dizisinin boyutu
histRange = (0, 256)   # Histogram dizisinin alacağı değerlerin aralığı

Hist = np.zeros(256)  # Hist dizisinin içini sıfır diziyle doldurma
w,h = foto.shape  # Girilen resmi eni ve boyu
#print(w,h)  #eni ve boyu bastırma

#
for i in range(0, w):
    for j in range(0,h):
         indks = foto[i,j]  # Resmin her pikselini gezip bunun değerini bir değişkene atıyoruz.
         Hist[indks] +=1    # O pikselin değeri kaçsa o dizinin o elemanını bir arttıyoruz.


# Histogram dizisini bastırma
for i,indks in enumerate(Hist):
    print(f"{i} -> {indks}")


