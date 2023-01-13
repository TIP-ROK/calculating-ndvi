import time
from colorsys import hsv_to_rgb
import geopandas as gp
import rasterio
from rasterio.features import shapes


start = time.time()


tiff_name = './output/cuttedNDVI.tiff'
data = rasterio.open(tiff_name).meta


c = str(data['crs'])
c_s = c.split(':')


mask = None
with rasterio.open(tiff_name) as src:
    image = src.read(1)  # first band
    results = (
    {'properties': {'NDVI': v}, 'geometry': s}
    for i, (s, v) in enumerate(shapes(image, mask=mask, transform=data['transform'])))


geoms = list(results)


gpd_polygonized_raster = gp.GeoDataFrame.from_features(geoms, crs=c)


gpd_polygonized_raster = gpd_polygonized_raster[gpd_polygonized_raster['NDVI']>0]


def pseudocolor(val, minval, maxval):
    """ Convert val in range minval..maxval to the range 0..120 degrees which
        correspond to the colors Red and Green in the HSV colorspace.
    """
    h = (float(val-minval) / (maxval-minval)) * 120

    # Convert hsv color (h,1,1) to its rgb equivalent.
    # Note: hsv_to_rgb() function expects h to be in the range 0..1 not 0..360
    r, g, b = hsv_to_rgb(h/360, 1., 1.)
    return int(r*255), int(g*255), int(b*255)


minval = 0
maxval = 1


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


for i, row in gpd_polygonized_raster.iterrows():
  gpd_polygonized_raster.loc[i, ('color')] = rgb_to_hex(pseudocolor(row['NDVI'], minval, maxval))
  gpd_polygonized_raster['id'] = gpd_polygonized_raster.index


crs_sys = 'epsg:' + c_s[1]
gpd_polygonized_raster['geometry'] = gpd_polygonized_raster['geometry'].to_crs({'init': crs_sys})
gpd_polygonized_raster.to_file('result.geojson', driver='GeoJSON')
print(time.time() - start)
