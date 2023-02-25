from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
import matplotlib.pyplot as plt


def mean_fits(fits_img):
    n = len(fits_img)
    if n > 0:
        hdulist = fits.open(fits_img[0])
        img_array = hdulist[0].data
        for i in range(1, n):
            img_array += fits.open(fits_img[i])[0].data
        mean = img_array / n

        return mean



def header_details(fits_img_index):
    fits_img = [z_img, g_img, i_img, r_img, u_img]
    if fits_img_index == 'z':
        hdulist = fits.open(fits_img[0])
        header = hdulist[0].header
        wcs = WCS(header)
        # print(header)

    elif fits_img_index == 'g':
        hdulist = fits.open(fits_img[1])
        header = hdulist[0].header
        wcs = WCS(header)
        # print(header)

    elif fits_img_index == 'i':
        hdulist = fits.open(fits_img[2])
        header = hdulist[0].header
        wcs = WCS(header)
        # print(header)

    elif fits_img_index == 'r':
        hdulist = fits.open(fits_img[3])
        header = hdulist[0].header
        wcs = WCS(header)
        # print(header)

    elif fits_img_index == 'u':
        hdulist = fits.open(fits_img[4])
        header = hdulist[0].header
        wcs = WCS(header)
        # print(header)

    return wcs.wcs.ctype[0], wcs.wcs.ctype[1]


if __name__ == '__main__':
    z_img = 'G:/Purdue/Spring 2023/Coursera/z.fits'
    g_img = 'G:/Purdue/Spring 2023/Coursera/g.fits'
    i_img = 'G:/Purdue/Spring 2023/Coursera/i.fits'
    r_img = 'G:/Purdue/Spring 2023/Coursera/r.fits'
    u_img = 'G:/Purdue/Spring 2023/Coursera/u.fits'

    data = mean_fits([z_img, g_img, i_img, r_img, u_img])
    bright_index = np.unravel_index(np.argmax(data, axis=None), data.shape)
    print(bright_index)

    # plotting results
    plt.imshow(data, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.colorbar()
    plt.show()
