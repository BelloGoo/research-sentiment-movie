import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PIL
from sklearn.cluster import KMeans
from collections import Counter
# %matplotlib inline


# def palette_perc(k_cluster):
#     width = 300
#     palette = np.zeros((50, width, 3), np.uint8)
    
#     n_pixels = len(k_cluster.labels_)
#     counter = Counter(k_cluster.labels_) # count how many pixels per cluster
#     perc = {}
#     for i in counter:
#         perc[i] = np.round(counter[i]/n_pixels, 2)
#     perc = dict(sorted(perc.items()))
    
#     #for logging purposes
#     print(perc)
#     print(k_cluster.cluster_centers_)
    
#     step = 0
    
#     for idx, centers in enumerate(k_cluster.cluster_centers_): 
#         palette[:, step:int(step + perc[idx]*width+1), :] = centers
#         step += int(perc[idx]*width+1)
        
#     return palette

def palette(clusters):
    width=300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width/clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_): 
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
    # print(clusters.cluster_centers_)
    # return palette
    return clusters.cluster_centers_

def show_img_compar(img_1, img_2 ):
    f, ax = plt.subplots(1, 2, figsize=(10,10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') #hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()

def read_resize(path):
    img = cv.imread(path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    dim = (500, 300)
    # resize image
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return img



img = read_resize(r"C:\Users\85270\Downloads\DNM65.png")
clt = KMeans(n_clusters=3)
clt = clt.fit(img.reshape(-1, 3))
print(palette(clt))
# show_img_compar(img, palette_perc(clt))