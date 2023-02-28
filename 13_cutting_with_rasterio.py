import json
import rasterio
from rasterio import mask

# Load the GeoTIFF file
with rasterio.open('./copernicus_dataspace/july/merged/B04.tif') as src:
    # Load the GeoJSON-like object containing the coordinates
    geojson_obj = '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"coordinates":[[[76.25564275328941,42.477663795725846],[76.25564275328941,42.47686842413566],[76.2560349000724,42.476006296888954],[76.25694739547197,42.477663795725846],[76.25564275328941,42.477663795725846]]],"type":"Polygon"}}]}'

    # Convert the GeoJSON-like object to a GeoJSON string
    geojson_str = json.loads(geojson_obj)

    # Mask the GeoTIFF file using the GeoJSON string
    out_image, out_transform = mask.mask(src, [geojson_str], crop=True)

    # Update the metadata for the new image
    out_meta = src.meta.copy()
    out_meta.update({
        "driver": "GTiff",
        "height": out_image.shape[1],
        "width": out_image.shape[2],
        "transform": out_transform
    })

    # Save the new GeoTIFF file
    with rasterio.open('./copernicus_dataspace/july/B04__cutted.tiff', 'w', **out_meta) as dst:
        dst.write(out_image)
