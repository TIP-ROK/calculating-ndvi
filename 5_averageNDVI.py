import numpy as np
import rasterio


def get_region_of_interest(ndvi, multiplier=1/2):

    # undo the background adjustment
    region = ndvi.copy()
    region = np.where(region == -255, 0, region)

    # mean of center rows
    center_row1 = np.mean(region[int((multiplier) *len(region))])
    center_row2 = np.mean(region[int((multiplier) *len(region))+1])

    # mean of both rows
    mean = (center_row1.copy()+center_row2.copy())/2
    return mean


my_file = rasterio.open('./output/2ndvi.tiff')
ndvi = my_file.read(1).astype('float64')


print(get_region_of_interest(ndvi=ndvi))
