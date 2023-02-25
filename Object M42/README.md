The Flexible Image Transport System (FITS) is a commonly used format for astronomical images. It stores the image as a numerical array, which can be loaded into a NumPy array. Additionally, FITS files have headers that contain metadata about the image.

To access FITS images of various celestial objects, one can visit the SDSS website and navigate to the https://dr12.sdss.org/fields. Upon opening a FITS file using Astropy, an HDU (Header/Data Unit) list is returned. Each HDU contains headers and, optionally, image data.

The header of each HDU object includes metadata such as its dimensions and data type. Image data can be present in any HDU. The first HDU in the list is the primary HDU.

Here, I have computed the mean of a set of FITS files for the object M42.
Mean stacking is a method that involves taking the mean of the pixel values at each position in the stack of images. Mean stacking can be effective at reducing noise in the final image, but it is less effective at removing cosmic rays and other artifacts.
