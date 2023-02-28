from osgeo import gdal
import traceback


def cutting_tiff(outputpath, inputpath, polygon):
    gdal.UseExceptions()
    try:
        cutted = gdal.Warp(destNameOrDestDS=f'{outputpath}',
                           srcDSOrSrcDSTab=inputpath,
                           cutlineDSName=f'{polygon}',
                           cropToCutline=True,
                           copyMetadata=True,
                           dstNodata=0)
    except Exception as e:
        print(f'exception == {e}')


cutting_tiff(outputpath='./output/cuttedNDVI.tiff', inputpath='./output/2ndvi.tiff', polygon='./cords.geojson')
