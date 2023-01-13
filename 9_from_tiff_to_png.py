import matplotlib.pyplot as plt
import numpy
import rasterio


image_file = "./output/cuttedNDVI.tiff"

with rasterio.open(image_file) as f:
    image = f.read(1)



fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)


cmap = plt.cm.YlGn
cax = ax.imshow(image, cmap=cmap)


ax.axis('on')
ax.set_title('Normalized Difference Vegetation Index', fontsize=18, fontweight='bold')


cbar = fig.colorbar(cax, orientation='horizontal', shrink=0.65)


ax.plot(20, 10)

plt.savefig('./output/cuttedresult.png', bbox_inches='tight', transparent=True)
plt.show()
