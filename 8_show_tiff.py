import rasterio
from rasterio import plot


with rasterio.open('./output/cuttedNDVI.tiff') as f:
    # Get the bounding box of the whole GeoTIFF file
    bbox = f.bounds
    print('Bounding box of the whole GeoTIFF file:', bbox)

    # Get the CRS (Coordinate Reference System) of the GeoTIFF file
    crs = f.crs
    print('CRS of the GeoTIFF file:', crs)

    # Get the transform matrix of the GeoTIFF file
    transform = f.transform
    print('Transform matrix of the GeoTIFF file:', transform)

    # Get the width and height of the GeoTIFF file in pixels
    width = f.width
    height = f.height
    print('Width and height of the GeoTIFF file in pixels:', width, height)
    plot.show(f)
