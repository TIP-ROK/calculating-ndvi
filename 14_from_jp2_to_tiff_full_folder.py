import os
import rasterio

input_folder = 'copernicus_dataspace/kemin/T43TEH_20220609T054651'
output_folder = 'copernicus_dataspace/kemin/T43TEH_20220609T054651_tiff'

for filename in os.listdir(input_folder):
    if filename.endswith('.jp2'):
        src_path = os.path.join(input_folder, filename)
        print(src_path)
        dst_path = os.path.join(output_folder, filename[:-3] + 'tif')

        with rasterio.open(src_path) as src:
            meta = src.meta.copy()
            meta.update(driver='GTiff')
            with rasterio.open(dst_path, 'w', **meta) as dst:
                dst.write(src.read())
