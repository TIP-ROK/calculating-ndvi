import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt




image_file = "./output/sentinel2.tif"
src = rasterio.open(image_file)
fig, (axb, axg, axr, axn) = plt.subplots(1,4, figsize=(24,8))
show((src, 1), ax=axb, cmap='Blues', title='Blue channel')
show((src, 2), ax=axg, cmap='Greens', title='Green channel')
show((src, 3), ax=axr, cmap='Reds', title='Red channel')
show((src, 4), ax=axn, cmap='Oranges', title='NIR channel')
plt.show()
