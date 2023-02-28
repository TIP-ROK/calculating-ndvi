from io import BytesIO

import matplotlib.pyplot as plt
import numpy
import numpy as np
import rasterio


def get_evi(red_file, nir_file, blue_file):
    with rasterio.open(red_file) as band_red:
        red = band_red.read(1).astype('float64')

    with rasterio.open(nir_file) as band_nir:
        nir = band_nir.read(1).astype('float64')

    with rasterio.open(blue_file) as band_blue:
        blue = band_blue.read(1).astype('float64')

    # Allow division by zero
    numpy.seterr(divide='ignore', invalid='ignore')

    # # Calculate evi
    evi = 2.5 * ((nir.astype(float) - red.astype(float)) / (nir + 6 * red - 7.5 * blue + 1))

    return evi


path = './kaium/cutted/'
print(get_evi(red_file=path + 'cutted_B04.tif', nir_file=path + 'cutted_B08.tif', blue_file=path + 'cutted_B02.tif'))
