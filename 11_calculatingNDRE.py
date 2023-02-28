import matplotlib.pyplot as plt
import numpy
import rasterio


with rasterio.open('./kaium/cutted/cutted_B07.tif') as f:
    band_red = f.read(1)

with rasterio.open('./kaium/cutted/cutted_B8A.tif') as file:
    band_nir = file.read(1)


numpy.seterr(divide='ignore', invalid='ignore')


# Calculate NDVI
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)


min = numpy.nanmin(ndvi)
max = numpy.nanmax(ndvi)
mid = 0.1


fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)


cmap = 'BrBG'
cax = ax.imshow(ndvi, cmap=cmap, clim=(min, max), vmin=min, vmax=max)


ax.axis('on')
ax.set_title('Normalized Difference Vegetation Index', fontsize=18, fontweight='bold')


cbar = fig.colorbar(cax, orientation='horizontal', shrink=0.65)


ax.plot(20, 10)

plt.savefig('./kaium/result.png', bbox_inches='tight', transparent=True)
plt.show()
plt.close()
