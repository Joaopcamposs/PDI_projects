import PySimpleGUI as sg
import os.path
import cv2
import numpy as np

def redim(img, largura): #função para redimensionar uma imagem
    alt = int(img.shape[0]/img.shape[1]*largura)
    img = cv2.resize(img, (largura, alt), interpolation = cv2.INTER_AREA)
    return img

def bandaRejeicao(img,D0=5,W=10):
    assert img.ndim == 2
    linhas, colunas = img.shape[1],img.shape[0]
    u, v = np.meshgrid(np.arange(linhas), np.arange(colunas))
    faixa = np.sqrt( (u-linhas/2)**2 + (v-colunas/2)**2 )
    estaNaFaixa = (faixa < (D0 - W / 2)) | (faixa > (D0 + W / 2))
    faixa[estaNaFaixa] = 1
    faixa[~estaNaFaixa] = 0
    return faixa

def rejeitaFaixa(img,D0=5,W=10):
    assert img.ndim == 2
    banda = bandaRejeicao(img,D0,W)
    cv2.namedWindow('Banda de rejeição')
    cv2.moveWindow('Banda de rejeição', 500,30)
    cv2.imshow('Banda de rejeição',banda)
    espectro = np.fft.fft2(img)
    espectro = np.fft.fftshift(espectro)
    espectroAbsoluto = np.absolute(espectro)
    espectroAbsoluto = espectroAbsoluto/espectroAbsoluto.max()*255
    espectroAbsoluto *= banda
    cv2.namedWindow('Espectro Fourier') 
    cv2.moveWindow('Espectro Fourier', 30,30)
    cv2.imshow('Espectro Fourier',espectroAbsoluto)
    espectro *= banda
    inversa = np.fft.ifftshift(espectro)
    inversa = np.fft.ifft2(inversa)
    inversa = np.abs(inversa)
    return inversa

def SUAFUNCAO(img, parametro, parametro2):

    #aplicando SUAFUNÇÃO
    print('Processando a Imagem')

    imgResult = rejeitaFaixa(img,parametro, parametro2)
    print(parametro)
    
    print('Salvando Imagem Saida ...')

    imgRed = redim(imgResult,320)
    cv2.imwrite('saida.png',imgRed)
    
    return imgResult

file_list_column = [
    [        
        sg.Text("Path image:"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        #sg.FolderBrowse(),
        sg.FileBrowse(file_types=(("TODOS", "*.*"),),initial_folder=(os.getcwd())),        
    ],
    [
        sg.Text("Frequencia central: "),sg.Slider(range=(0, 100), orientation='h', size=(20, 20), default_value=0,key='-PARAMETRO1-')
    ],
    [
        sg.Text("Largura de banda: "),sg.Slider(range=(0, 200), orientation='h', size=(20, 20), default_value=0,key='-PARAMETRO2-')
    ],
    [
        sg.Button('Update',key='-BUTTON-')
    ]
]

# For now will only show the name of the file that was chosen

image_viewer_column = [
    [sg.Text("Imagem Original:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")]
    
]

image_viewer_column2 = [
    [sg.Text("Imagem de Saída:")],
    [sg.Text(size=(40, 1), key="-TOUT2-")],
    [sg.Image(key="-IMAGE2-")],
    [sg.Image(key="-IMAGE3-")]
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column2),
    ]
]

window = sg.Window("Visualizador de Imagens", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    # Folder name was filled in, make a list of files in the folder

    if event == "-FOLDER-":
        print('Procurando Imagem...')
        folder = values["-FOLDER-"]
        filename = values["-FOLDER-"]
        parametro1 = int( values['-PARAMETRO1-'])
        parametro2 = int( values['-PARAMETRO2-'])
           
        try:            
            
            imgOriginal = cv2.imread(filename,0)
            print('Abrindo Imagem...')

            imgOrigRed = redim(imgOriginal,320)
            cv2.imwrite('imgOriginalRed.png',imgOrigRed)

            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename='imgOriginalRed.png')

            try:
                print('Inicio Processamento...')
                nome = SUAFUNCAO(imgOriginal,parametro1, parametro2)
                window["-TOUT2-"].update('saida.png')
                window["-IMAGE2-"].update(filename='saida.png')
            except:
                print('Impossível fazer o Processamento ...')
                pass
 
        except:
            print("Imagem não encontrada.")
            pass

    if event == '-BUTTON-':
        print('Atualizando Imagem de Saída ...')
        folder = values["-FOLDER-"]
        filename = values["-FOLDER-"]
        parametro1 = int (values['-PARAMETRO1-'])
        parametro2 = int( values['-PARAMETRO2-'])

        imgOriginal = cv2.imread(filename,0)
        print('REabrindo Imagem...')
           
        try:            
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename='imgOriginalRed.png')

            print('Refazendo Processamento ...')
            nome = SUAFUNCAO(imgOriginal,parametro1, parametro2)

            window["-TOUT2-"].update('saida.png')
            window["-IMAGE2-"].update(filename='saida.png')

        except:
            print('Impossível REfazer o Processamento ...')
            pass

window.close()