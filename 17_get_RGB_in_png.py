# %%
import matplotlib.pyplot as plt
import numpy as np
import rasterio
import os
from osgeo import gdal

# %%
fp_in = 'rgb/'
fp_out = 'rgb/'

fn_blue = 'B02'
fn_green = 'B03'
fn_red = 'B04'

# %%
band_02=rasterio.open(fp_in+fn_blue+'.tif')
band_03=rasterio.open(fp_in+fn_green+'.tif')
band_04=rasterio.open(fp_in+fn_red+'.tif')

# %%
red = band_04.read(1)
green = band_03.read(1)
blue = band_02.read(1)

# %%
# rgb_composite_raw= np.dstack((red, green, blue))
# rgb_composite_raw.shape

# %%
def normalize(band):
    band_min, band_max = (band.min(), band.max())
    return ((band-band_min)/((band_max - band_min)))

red_n = normalize(red)
green_n = normalize(green)
blue_n = normalize(blue)

# %%
rgb_composite_n= np.dstack((red_n, green_n, blue_n))
plt.imshow(rgb_composite_n)

# %% [markdown]
# Finally we can see our area of interest, however the colors seem to be not really realistic and the whole image is a bit dark.
#
# ## Basic image manipulation techniques
# To solve this issue, we will have to brighten each band first, then normalize them and do the stacking.
# From mathematical point of view, the brightening function multiplies each pixel value with 'alpha' and adds 'beta' value if necessary.
# If this operation is done we have to clip the resulted pixel values between 0..255.

# %%
def brighten(band):
    alpha=0.13
    beta=0
    return np.clip(alpha*band+beta, 0,255)

red_b=brighten(red)
blue_b=brighten(blue)
green_b=brighten(green)

red_bn = normalize(red_b)
green_bn = normalize(green_b)
blue_bn = normalize(blue_b)

# %%
rgb_composite_bn= np.dstack((red_bn, green_bn, blue_bn))
plt.imshow(rgb_composite_bn)

# %% [markdown]
# Now our image is looking quite realistic now. Note that this image does not represent the real reflectance values.
#
# Another image manipulation technique is gamma correction. The math behind it is that we take each pixels intesnity values and raise it to the power of (1/gamma) where the gamma value is specified by us.
# Let's use our raw images, do the gamma correction and normalization.

# %%
def gammacorr(band):
    gamma=2
    return np.power(band, 1/gamma)

red_g=gammacorr(red)
blue_g=gammacorr(blue)
green_g=gammacorr(green)

red_gn = normalize(red_g)
green_gn = normalize(green_g)
blue_gn = normalize(blue_g)

# %%
rgb_composite_gn= np.dstack((red_gn, green_gn, blue_gn))
plt.imshow(rgb_composite_gn)

# %% [markdown]
# Saving the image into PNG
# What most people want to do at this point is to save the image into a file.
# This could be done with the following lines of code will save the brightened and normalized image into a PNG file.
# Notice that an interpolation method is given to smooth the image and also the dpi value can be controlled.
# For more info please visit Pyplot documentation.

# %%
rgb_plot=plt.imshow(rgb_composite_bn, interpolation='lanczos')
plt.axis('off')
plt.savefig(fp_out+'tihany_rgb_composite.png',dpi=200,bbox_inches='tight')

rgb_plot_1 = plt.imshow(rgb_composite_gn, interpolation='lanczos')
plt.axis('off')
plt.savefig(fp_out+'tihany_rgb_composite_gn.png',dpi=200,bbox_inches='tight')
plt.close('all')
