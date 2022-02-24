#processo_imagem.py

import cv2
imagem = cv2.imread('Frutas.jpg')
print('Resolução: ', imagem.shape)
print('Total de pixels: ', imagem.size)


#obtem a cor de um único pixel
valorPixel = imagem[150,150]
print('Intensidade RGB: ', valorPixel)


#converte para cinza e obtém a cor
cinza = cv2.cvtColor(imagem,cv2.COLOR_RGB2GRAY)

valorPixel = cinza[150,150]
print('Cinza: ', valorPixel)


#Altera a cor de um único pixel

imagem[150,150] = [255,255,255]

#altera cor da linha 150 na imagem, criando um traço branco
for coluna in range (0,500):
    imagem[150,coluna] = [255,255,255]

cv2.imshow('Pixel Alterado', imagem)
