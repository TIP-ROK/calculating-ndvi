from osgeo import gdal, osr

in_path = 'ds/20220428/tif/'
input_filename = 'T43TCH_20220428T055629_B02_20m.tif'

out_path = 'ds/20220428/gdal_cut-1/'
output_filename = 'tile_'

tile_size_x = 256
tile_size_y = 256

src_ds = gdal.Open(in_path + input_filename)
src_srs = osr.SpatialReference(wkt=src_ds.GetProjection())

dst_srs = osr.SpatialReference()
dst_srs.ImportFromEPSG(4326)

transform = osr.CoordinateTransformation(src_srs, dst_srs)

xsize = src_ds.RasterXSize
ysize = src_ds.RasterYSize

for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        xmin = i
        ymin = j
        xmax = i + tile_size_x
        ymax = j + tile_size_y
        if xmax > xsize:
            xmax = xsize
        if ymax > ysize:
            ymax = ysize
        dst_filename = out_path + output_filename + str(i) + "_" + str(j) + ".tif"
        gdal.Warp(dst_filename, src_ds, format='GTiff', outputBounds=[xmin, ymin, xmax, ymax], xRes=0.0001, yRes=0.0001, dstSRS='EPSG:4326')
