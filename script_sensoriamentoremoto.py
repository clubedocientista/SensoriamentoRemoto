'''
Clube do Cientista
    Aulão exclusivo 26/11/2020
    Sensoriamento remoto
    Processamento Digital de Imagens de Satélites com Python

Desenvolvido por: Rafael Menezes
    Colaboração: Gustavo Ferreira e Gustavo Baptista

Dados:
    Landsat 8 OLI
    30 de agosto de 2020
'''

# importando pacotes
from os import chdir
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
from spectral import imshow

# abrindo diretório
chdir ('D:\\Documentos\\Clube do Cientista\\cursos\\Discord\\Python_sensoriamento\\')

# lendo arquivos .tif
b2 = Image.open('B02.tif')
b3 = Image.open('B03.tif')
b4 = Image.open('B04.tif')
b5 = Image.open('B05.tif')
#b6 = Image.open('B06.tif')
b7 = Image.open('B07.tif')

# convertendo em .tif para np.array
b2array = np.array(b2)
b3array = np.array(b3)
b4array = np.array(b4)
b5array = np.array(b5)
#b6array = np.array(b6)
b7array = np.array(b7)

# verificando formatos, dimensões e bits
type(b2)
type(b2array)
b2.size
b2array.shape
b2array.dtype

# aplicando expansão de constrate nas bandas
imshow(b2array) # original
plt.show()
imshow(b2array,stretch = 0.02) # expansão de contraste 2%
plt.show()

# normalizando bandas
print('b2array -> ', np.min(b2array) , ' a ' , np.max(b2array))
print('b5array -> ', np.min(b5array) , ' a ' , np.max(b5array))

def norm(band):
    return band/2**(16)

b2arnorm = norm(b2array)
b3arnorm = norm(b3array)
b4arnorm = norm(b4array)
b5arnorm = norm(b5array)
#b6arnorm = norm(b6array)
b7arnorm = norm(b7array)

# RGB 
# matplotlib
rgb = np.dstack((b7arnorm,b5arnorm,b3arnorm)) # R7G5B3
plt.imshow(rgb)

rgb2 = np.dstack((b2arnorm,b3arnorm,b4arnorm)) # R2G3B4

imshow(rgb,bands = (0,1,2))                # (r,g,b)
imshow(rgb,bands = (0,1,2),stretch = 0.02) # 2% de expansão do histograma

# ou 
# PIL (pacote)
rgbArray = np.zeros((b3array.shape[0],b3array.shape[1],3), 'uint8') 
rgbArray[..., 0] = np.uint8(b7arnorm*256)  # R
rgbArray[..., 1] = np.uint8(b5arnorm*256)  # G
rgbArray[..., 2] = np.uint8(b3arnorm*256)  # B

Image.fromarray(rgbArray).show()


# Comprimento de onda das bandas de um determinado pixel
stack     = np.dstack((b2arnorm,b3arnorm,b4arnorm,b5arnorm,b7arnorm)) # empilhamento das bandas
comp_onda = [0.48,0.56,0.65,0.85,2.2] # valores comprimento de onda, em micrometros, das bandas
plt.plot(comp_onda,stack[108,126])
plt.xticks(comp_onda)
plt.xlabel('Comprimento de onda (micrômetros)',fontsize = 14, labelpad = 10)
plt.ylabel('Digital Number',fontsize = 14, labelpad = 10)


## Aplicação de índices espectrais
# (A - B) / (A + B)

# NDVI
# A = b5; B = b4
ndvi = (b5arnorm - b4arnorm)/(b5arnorm + b4arnorm)
Image.fromarray(ndvi*255.999).show()

# NDWI
# A = b5; B = b3
ndwi = (b5arnorm - b3arnorm)/(b5arnorm + b3arnorm)
imshow(ndwi,stretch = 0.02)
