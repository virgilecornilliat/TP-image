import numpy as np
import matplotlib.pyplot as plt

#création de l'image
image=np.array([[(0,0,0)]*91]*91)

#on donne à chaque pixel la couleur 'blanc'
image[:,:]=(255,255,255)
#plt.imshow(image)
#plt.show()

#on donne à chaque pixel la couleur 'vert'
image[:,:]=(0,255,0)
#plt.imshow(image)
#plt.show()

#affichage du triplet couleur du premier et dernier pixel
print(image[0,0], image[-1,-1])

#création du quadrillage bleu
for i in range(10):
    image[10*i,:]=(0,0,255) #on donne à 1 ligne sur 10 la couleur 'bleu'
    image[:,10*i]=(0,0,255) #on donne à 1 colonne sur 10 la couleur 'bleu'

#affichage
#plt.imshow(image)
#plt.show()

## Lecture et affichage d'une image en couleur

image2=plt.imread("data/les-mines.jpg").copy() #on réalise une copie pour pouvoir la modifier
#plt.imshow(image2)
#plt.show()

print(type(image2))
print(image2.ndim)
print(image2.shape[:2])
print(image2.itemsize)
print(image2.dtype)
print(image2.min(),image2.max())

#plt.imshow(image2[:10,:10])
#plt.show()


# On ne sélectionne qu'une ligne sur 2, 5, 10 puis 20. On crée une liste contenant ces valeurs :

L=[2,5,10,20]

# Pour chaque pas on crée l'image correspondante

#for pas in L:
    #plt.imshow(image2[:,::pas])
    #plt.show()


# On crée une fonction pour isoler le rectangle de dimensions l et c au centre de l'image

def isoler(l,c,image):
    h=len(image)
    larg=len(image[0])
    plt.imshow(image[(h-l)//2:(h+l)//2 , (larg-c)//2:(larg+c)//2])
    plt.show()

#isoler(10,20,image2)
#isoler(100,200,image2)

# On crée 3 tableaux stockant les valeurs de rouge, vert et bleu de l'image

red=image2[:,:,0]
green=image2[:,:,1]
blue=image2[:,:,2]

# Affichage

'''
plt.imshow(red, cmap="Reds")
plt.show()
plt.imshow(red, cmap="Greens")
plt.show()
plt.imshow(red, cmap="Blues")
plt.show()
'''

# Rectangle blanc rayé de rouge en bas à droite 

image3=image2.copy()
#image3[-200::,-200::]=(219, 112, 147)
image3[-200::,-200::]=(255,255,255)
image3[-200::10,-200::]=(255,0,0)
#plt.imshow(image3)
#plt.show()
#plt.imshow(image3[-20::,-20::])
#plt.show()

# Image transparente 

image4=plt.imread("data/les-mines.jpg")
h,w=image4.shape[:2]
#image5=np.array([[(0,0,0,0)]*w]*h)
image5=np.empty((h,w,4), dtype=image4.dtype)
image5[:,:,:3]=image4
image5[:,:,3]=128
#plt.imshow(image5)
#plt.show()

# Images en niveaux de gris 

image6=image4/255
image6_gris=image6.mean(axis=2)
image7_gris = 0.299 * image6[:,:,0] + 0.587 * image6[:,:,1] + 0.114 * image6[:,:,2]

plt.imshow(image7_gris, cmap="gray")
plt.show()

