import cv2
import os
import numpy as np
import rasterio

# Открываем входной файл с помощью Rasterio
with rasterio.open(f'10m/rgb_tif/T42TXK_20220526T060641_B02_10m.tif') as blue_band:
    # Читаем каналы красного, зеленого и синего цветов
    blue = blue_band.read(1)

with rasterio.open(f'10m/rgb_tif/T42TXK_20220526T060641_B03_10m.tif') as green_band:
    # Читаем каналы красного, зеленого и синего цветов
    green = green_band.read(1)

with rasterio.open(f'10m/rgb_tif/T42TXK_20220526T060641_B04_10m.tif') as red_band:
    # Читаем каналы красного, зеленого и синего цветов
    red = red_band.read(1)

# Масштабируем значения пикселей до диапазона от 0 до 255
red = np.interp(red, (red.min(), red.max()), (0, 255)).astype('uint8')
green = np.interp(green, (green.min(), green.max()), (0, 255)).astype('uint8')
blue = np.interp(blue, (blue.min(), blue.max()), (0, 255)).astype('uint8')

# Изменяем яркость и насыщенность каждого канала
brightness = 50
saturation = 1.5

red = cv2.convertScaleAbs(red, alpha=1, beta=brightness)
red = cv2.convertScaleAbs(red, alpha=saturation)

green = cv2.convertScaleAbs(green, alpha=1, beta=brightness)
green = cv2.convertScaleAbs(green, alpha=saturation)

blue = cv2.convertScaleAbs(blue, alpha=1, beta=brightness)
blue = cv2.convertScaleAbs(blue, alpha=saturation)

# Создаем RGB изображение, объединив каналы в одно изображение
rgb = np.dstack((red, green, blue))

# Получаем метаданные из исходного файла и обновляем количество каналов и тип данных
meta = green_band.meta.copy()
meta.update(count=3, dtype='uint8')

# Записываем RGB изображение в новый файл в формате GeoTIFF
with rasterio.open(f"10m/rgb_tif/RGB.tif", 'w', **meta) as dst:
    dst.write(rgb.transpose(2, 0, 1))
