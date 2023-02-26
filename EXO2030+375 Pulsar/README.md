The Flexible Image Transport System (FITS) is a widely used format for storing astronomical images as numerical arrays. FITS files also contain headers with metadata about the image. To access FITS images, visit the SDSS website and go to https://dr12.sdss.org/fields. When opening a FITS file using Astropy, an HDU (Header/Data Unit) list is returned, which contains headers and image data. Each HDU's header contains metadata about its dimensions and data type, and any HDU may have image data.

In astronomical imaging, different filters or "bands" are used to observe the sky at various wavelengths. Each filter allows a specific range of wavelengths to pass through, creating images that capture particular features of celestial objects. The Sloan Digital Sky Survey uses five bands:

u-band: Ultraviolet, sensitive to blue light, useful for detecting faint, blue objects.
g-band: Green, sensitive to green light, useful for studying galaxy properties.
r-band: Red, sensitive to red light, useful for measuring star and galaxy brightness.
i-band: Infrared, sensitive to longer-wavelength light than the red band, useful for detecting faint, red objects.
z-band: Near-infrared, sensitive to even longer-wavelength light than the i-band, useful for studying very faint galaxies and quasars.

Stacking images from different bands can create composite images that capture the objects' characteristics across all bands. Mean stacking is a method of taking the mean of the pixel values at each position in the stack of images.

In this project on the pulsar EXO 2030+375, I have computed the mean and median of a set of FITS files in various bands, including z-band, r-band, and others. EXO 2030+375 is a high-mass X-ray binary (HMXB) system consisting of a pulsar orbiting a massive companion star. The pulsar has a spin period of about 41.03 seconds and a magnetic field about 10^12 gauss, making it one of the most magnetized neutron stars known. The companion star is estimated to be a B0.5 Ib supergiant with a mass about 20 times that of the Sun.

                                            
![My Image](https://github.com/arijeetnath12/Data-driven-astronomy-with-Python/blob/689872ea72d12debb72f2f28b78bf362d1a9d020/EXO2030+375%20Pulsar/medianstack.jpeg)
                      Median Stack

![My Image](https://github.com/arijeetnath12/Data-driven-astronomy-with-Python/blob/70e612bd51752784d47dc21c01d47ece9f37a793/EXO2030+375%20Pulsar/meanstack.jpeg)
                      Mean Stack
