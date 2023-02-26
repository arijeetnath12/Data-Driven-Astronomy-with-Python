import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


def median_fits(img_list):
    fits_list = []  # create an empty list that would store the arrays from the image list

    for img in img_list:
        hdulist = fits.open(img)  # unpack the fits images
        fits_list.append(hdulist[0].data)  # append the pixel arrays to fits_list
    fits_list = np.array(fits_list)  # convert into numpy array to use .nbytes in memory calc

    # the fits_list array is a 3D array with shape (5, 1489, 2048) if img_list has 5 images
    # it basically means you have 2 images with each image having a 1489*2048 shape
    # therefore since we want median of a pixel over every fits file, we calculate the median across axis 0 which
    # corresponds to 5 in shape (5, 1489, 2048)

    median_img = np.median(fits_list, axis=0)

    return median_img,fits_list

if __name__ == '__main__':
    z_img = 'G:/Purdue/Spring 2023/Coursera/EXO2030+375_z.fits'
    g_img = 'G:/Purdue/Spring 2023/Coursera/EXO2030+375_g.fits'
    i_img = 'G:/Purdue/Spring 2023/Coursera/EXO2030+375_i.fits'
    r_img = 'G:/Purdue/Spring 2023/Coursera/EXO2030+375_r.fits'
    u_img = 'G:/Purdue/Spring 2023/Coursera/EXO2030+375_u.fits'

    result = median_fits([z_img,g_img,i_img,r_img,u_img])
    print(np.shape(result[1]))

    # plot results
    plt.imshow(result[0], cmap=plt.cm.nipy_spectral_r)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.show()