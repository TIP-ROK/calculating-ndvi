from osgeo import gdal
import os

in_path = 'ds/20220428/tif/'
input_filename = 'T43TCH_20220428T055629_B04_20m.tif'

out_path = 'ds/20220428/cutting_1/'
output_filename = 'tile_B04_'

tile_size_x = 640
tile_size_y = 640

ds = gdal.Open(in_path + input_filename)
band = ds.GetRasterBand(1)
xsize = band.XSize
ysize = band.YSize

for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        com_string = "gdal_translate -of GTIFF -srcwin " + str(i) + ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(in_path) + str(input_filename) + " " + str(out_path) + str(output_filename) + str(i) + "_" + str(j) + ".tif"
        os.system(com_string)
