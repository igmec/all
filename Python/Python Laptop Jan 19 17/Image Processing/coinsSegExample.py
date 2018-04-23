import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import matplotlib.patches as mpatches

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb
from skimage.segmentation import random_walker
from skimage.data import binary_blobs
import sys






image = data.coins()[50:-50, 50:-50]
#image = ndi.imread('C:\\Users\\Igor\\Desktop\\gray_tiny2sq.png', flatten=True)

# apply threshold
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
cleared = bw.copy()
#clear_border(cleared)

# label image regions
label_image = label(cleared)
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
ax.imshow(image_label_overlay)

for region in regionprops(label_image):

    # skip small images
    if region.area < 100:
        continue

    # draw rectangle around segmented coins
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)

plt.show()











sys.exit(0)







# Generate noisy synthetic data
data = ndi.imread('gray_tiny2sq.png', flatten=True)
data = skimage.img_as_bool(data)
data = skimage.img_as_float(data)

data += 0.1 * np.random.randn(*data.shape)


plt.imshow(data, cmap='gray', interpolation='nearest')
plt.show()


markers = np.zeros(data.shape, dtype=np.uint)
markers[data < -0.1] = 1
markers[data > 1.1] = 2


labels = random_walker(data,markers)
'''
#========================
# Generate noisy synthetic data
data = skimage.img_as_float(binary_blobs(length=128))

plt.imshow(data, cmap='gray', interpolation='nearest')
plt.show()

data += 0.35 * np.random.randn(*data.shape)


plt.imshow(data, cmap='gray', interpolation='nearest')
plt.show()

markers = np.zeros(data.shape, dtype=np.uint)
markers[data < -0.3] = 1
markers[data > 1.3] = 2

# Run random walker algorithm
labels = random_walker(data, markers, beta=10, mode='bf')
#========================
'''

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.2),
                                    sharex=True, sharey=True)
ax1.imshow(data, cmap='gray', interpolation='nearest')
ax1.axis('off')
ax1.set_adjustable('box-forced')
ax1.set_title('Noisy data')
ax2.imshow(markers, cmap='hot', interpolation='nearest')
ax2.axis('off')
ax2.set_adjustable('box-forced')
ax2.set_title('Markers')
ax3.imshow(labels, cmap='gray', interpolation='nearest')
ax3.axis('off')
ax3.set_adjustable('box-forced')
ax3.set_title('Segmentation')

fig.tight_layout()
plt.show()


sys.exit(0)

plt.imshow(data, cmap='gray', interpolation='nearest')
plt.show()
