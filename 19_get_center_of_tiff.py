import os

import rasterio
from osgeo import gdal, osr
from pyproj import Proj, transform


def get_epsg(ref):
    if ref.IsProjected():
        return int(ref.GetAuthorityCode("PROJCS"))
    elif ref.IsGeographic():
        return int(ref.GetAuthorityCode("GEOGCS"))


def get_center_point(file_path):
    raster = gdal.Open(file_path)
    gt = raster.GetGeoTransform()
    # get EPSG
    projection = raster.GetProjection()
    spatial_ref = osr.SpatialReference()
    spatial_ref.ImportFromWkt(projection)
    epsg = get_epsg(spatial_ref)
    width = raster.RasterXSize
    height = raster.RasterYSize

    centerX = gt[0] + width * gt[1] / 2 + height * gt[2] / 2
    centerY = gt[3] + width * gt[4] / 2 + height * gt[5] / 2
    inProj = Proj(init=f'epsg:{epsg}')
    outProj = Proj(init='epsg:4326')
    x1, y1 = centerX, centerY
    x2, y2 = transform(inProj, outProj, x1, y1)

    # return centerX, centerY
    return x2, y2


fp_in = "./jp2/R20m-ton-1-out/cutted/tile_0-0_B04.tif"
center_point = get_center_point(fp_in)

print("Center point coordinates: ", center_point)
