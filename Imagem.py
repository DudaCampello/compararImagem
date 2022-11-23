from PIL import Image

image = Image.open("foto/imagem1.jpg")  # carregar imagem
print(image.format)  # imprimindo propriedade da imagem - formato
print(image.mode)  # propriedade da imagem - Red-Green-Blue RGB
print(image.size)  # propriedade da imagem - tamanho

# A faixa de valor de bits é de 0 até 255 - se a combinacao de valor for 255=branco, 0=preto

# para trabalhar com matriz usamos a biblioteca numpy

from matplotlib import image  # bibliotecas para visualizar imagens
from matplotlib import pyplot

# transformar a imagem digital num array numpy

data = image.imread("foto/imagem1.jpg")  # data=dado - carregando imagem
print(data)  # mostra datatype do tipo array. Para cada unidade tres valores/cor
print(data.dtype)  # mostra o tipo de dados (uint8)
print(data.shape)  # mostra forma (115, 173, 3)
print(data.min())  # 0
print(data.max())  # 255

pyplot.imshow(data)                   # exibir array de pixels como imagem digital
image2 = Image.fromarray(data)        # converter o array de pixels em um objeto Image Pillow
type(image2)                          # verificando o tipo do objeto
image2: Image = Image.fromarray(data)

from numpy import asarray               # convertendo um objeto do tipo imagem para um array numpy

image = Image.open('foto/imagem1.jpg')  # carregando novamente a imagem usando metodo open da classe image
data = asarray(image)

print(data.dtype)   # mostra o tipo de dados (uint8)
print(data.shape)   # mostra forma (115, 173, 3)

image.save("foto/imagem1.jpg", format="PNG")
image.save("foto/imagem1.jpg", format="GIF")

image_cinza = image.convert(mode="L")  # convertendo em cinza
image_cinza.save("foto/imagem1.jpg")

image.thumbnail((100, 100))     # diminui o tamanho da escala
print(image.size)               # verificando o tamanho 100,66

image_resize = image.resize((200, 200))  # define tamanho padrão da base de dados
print(image_resize.size)                 # 200, 200
pyplot.imshow(image_resize)
image_resize: Image = image.resize((200, 200))

# horizontal_image = image.transpose(Image.FLIP_LEFT_RIGHT)   # Inverte imagem - horizontal
# pyplot.imshow(horizontal_image)
#horizontal_image: Image = image.transpose(Image.FLIP_LEFT_RIGHT)

# vertical_image = image.transpose(Image.FLIP_TOP_BOTTOM)
# pyplot.imshow(vertical_image)
# vertical_image: Image = image.transpose(Image.FLIP_TOP_BOTTOM)


# normalizando valores de pixel
image = Image.open("foto/imagem1.jpg")
pixels = asarray(image)                     # convertendo a imagem num array
pixels = pixels.astype('float32')           # convertendo os valores em float para realizar normalização
pixels /= pixels.max()                      # normaliza a faixa de valores


print('Data Type: %s' % pixels.dtype)                            # float32
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))    #Min: 0.063, Max: 1.000

import cv2
def orb_sim(img1, img2):
    orb = cv2.ORB_create()






