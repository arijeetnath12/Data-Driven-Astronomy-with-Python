from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from astroscrappy import detect_cosmics
import matplotlib.pyplot as plt
from astropy.wcs import WCS
from scipy.ndimage.filters import laplace
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.visualization.wcsaxes import WCSAxes


#Load Input image
hdulist = fits.open('frame-u-003630-1-0177.fits')
data = hdulist[0].data
header = hdulist[0].header
wcs = WCS(header)
print(wcs)
print(np.shape(data))
crpix_ra = header['CRPIX1']
crpix_dec = header['CRPIX2']


#calculate image statistics and normalize the image for plotting
#sigma_clipped_stats returns mean,median,std after rejecting outlier pixel
# above or below 'sigma' std deviation from the computed mean
mean,median,std = sigma_clipped_stats(data, sigma=3.0)
norm = ImageNormalize(vmin = median - 3*std, vmax = median + 10*std, stretch = SqrtStretch())



# Use the L.A.Cosmic algorithm to remove cosmic rays
cleaned_hdulist = detect_cosmics(data, sigclip=9.0, sigfrac=0.8, objlim=10.0)
cleaned_data = cleaned_hdulist[1].data  # extract the cleaned image data from the second extension


# plot the original and cleaned image
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.imshow(data, cmap='gray', origin='upper', norm=norm)
ax1.set_title('Original Image')

ax2.imshow(cleaned_data, cmap='gray', origin='upper', norm=norm)
ax2.set_title('Cleaned Image')

# subtract the cleaned image from the original image to highlight differences
diff_data = data - cleaned_data
ax3.imshow(diff_data, cmap='gray', origin='upper', norm=norm)
ax3.set_title('Difference Image')

plt.show()
