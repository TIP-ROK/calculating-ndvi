import rasterio
from rasterio import plot


with rasterio.open('./output/cuttedNDVI.tiff') as f:
    plot.show(f)
    