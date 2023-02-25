The Flexible Image Transport System (FITS) is a commonly used format for astronomical images. It stores the image as a numerical array, which can be loaded into a NumPy array. Additionally, FITS files have headers that contain metadata about the image.

To access FITS images of various celestial objects, visit the SDSS website and navigate to the https://dr12.sdss.org/fields. Upon opening a FITS file using Astropy, an HDU (Header/Data Unit) list is returned. Each HDU contains headers and, optionally, image data.

The header of each HDU object includes metadata such as its dimensions and data type. Image data can be present in any HDU.

In astronomical imaging, the different bands (such as z-band, r-band, etc.) refer to different filters used to observe the sky at different wavelengths. Each filter allows light in a specific range of wavelengths to pass through while blocking the rest, creating an image that captures a particular feature or characteristic of the object or region being observed.
Here's a brief description of each of the five bands used by the Sloan Digital Sky Survey:

u-band: This is the ultraviolet band, with a central wavelength of approximately 355 nm and a bandwidth of about 46 nm. It is sensitive to bluer light and is useful for detecting faint, blue objects.

g-band: This is the green band, with a central wavelength of approximately 480 nm and a bandwidth of about 150 nm. It is sensitive to green light and is useful for studying the properties of galaxies.

r-band: This is the red band, with a central wavelength of approximately 625 nm and a bandwidth of about 138 nm. It is sensitive to red light and is useful for measuring the brightness of stars and galaxies.

i-band: This is the infrared band, with a central wavelength of approximately 769 nm and a bandwidth of about 153 nm. It is sensitive to longer-wavelength light than the red band and is useful for detecting faint, red objects.

z-band: This is the near-infrared band, with a central wavelength of approximately 920 nm and a bandwidth of about 150 nm. It is sensitive to even longer-wavelength light than the i-band and is useful for studying very faint galaxies and quasars.

I have computed the mean of a set of FITS files which are the z-band, r-band, etc  for the object M42. Stacking images from different bands can produce a composite image that captures the characteristics of the objects in all the bands.Mean stacking is a method that involves taking the mean of the pixel values at each position in the stack of images. The resulting composite image contain information from all the bands and can reveal different features of the objects in the image, such as their colors or brightness in different parts of the spectrum.


