#meu_paint.py


#biblioteca oepn cv = computação visual
import cv2

def eventoClick(evento,x,y,flags,param):
    if evento == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        pt = [x,y]
        #altera cor do pixel
        img = cv2.circle(imagem,pt,20,cor,-1)
        cv2.imshow('Meu Photoshop', imagem)
#RGB
cor = [255,255,255]

imagem = cv2.imread('frutas.jpg')
cv2.imshow('Meu Photoshop', imagem)

cv2.setMouseCallback('Meu Photoshop', eventoClick)


cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('E:/Curso Python - Andre Mayer/Aula 07/frutas_paint.jpg',imagem)
