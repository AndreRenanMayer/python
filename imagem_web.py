#image_web.py
#pip install scikit-image
#pip install pafy
#pip install --upgrade youtube_dl


import cv2
from skimage import io
import pafy


#mostra imagem da web
def mostraWeb():
    imagem = io.imread('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsr6TSnWML6TvRXXoEntOlV4lc4mWgqzb7Pg&usqp=CAU')
    cv2.imshow('Imagem Web', imagem)
                       

def exibeQuadro():
    captura = cv2.VideoCapture('video.mp4')
    ret, frame = captura.read()
    cv2.imshow('Exibinddo um quadro do video', frame)


def exibeVideo():

    #ude parametro (0)para capturar da webcam
    #captura = cv2.VideoCapture(0)

    captura = cv2.VideoCapture('video.mp4')

    while True:
        ret, frame = captura.read()
        cv2.imshow('Exibindo um quadro do video', frame)
        cv2.waitKey(2)

        if cv2.waitKey(25) & 0xFF == ord('s'):
            break

    captura.release()
    cv2.destroyAllWindows()

def exibeYoutube():
    url = 'https://www.youtube.com/watch?v=6TJwFWVjOJU'
    video = pafy.new(url)
    best = video.getbest()
    captura=cv2.VideoCapture(best.url)


    while True:

        ret, frame = captura.read()
        cv2.imshow('Exibindo video do YouTube',frame)
        cv2.waitKey(25)
    
    
        
#mostraWeb()
#exibeQuadro()
#exibeVideo()
exibeYoutube()
