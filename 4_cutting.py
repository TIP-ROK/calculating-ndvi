from osgeo import gdal


def cutting_tiff(outputpath, inputpath, polygon):
    gdal.Warp(destNameOrDestDS=f'{outputpath}',
              srcDSOrSrcDSTab=inputpath,
              cutlineDSName=f'{polygon}',
              cropToCutline=True,
              copyMetadata=True,
              dstNodata=0)


cutting_tiff(outputpath='./output/cuttedNDVI.tiff', inputpath='./output/2ndvi.tiff', polygon='./cords.geojson')
