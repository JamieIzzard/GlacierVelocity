# GlacierVelocity

## Project Description
Tools related to Glacier Velocity Measurements. Contains scripts to process satellite imagery into ice velocity maps and analyze the outputs. Created and maintained by Jamie Izzard, June 2023. As of this version, it probably won't work on other systems, but I plan to improve compatibility in the future. So far, it's only set up for Sentinel-1 SLCs, but only minor changes are needed for other imagery.

## Prerequisites
- This toolbox requires access to a GAMMA remote sensing license and has been built and tested on the version released 2022/11/29.
- This code accesses GAMMA functions through the Python wrapper 'py_gamma'.
- Built and tested on Python 3.9.7.

## Content
The code is currently located in the tests directory. When it has been fully tested, it will be moved to a more appropriate location. 

The code is split into three files:
1. `processing.py` - Contains all of the functions for processing SAR imagery into velocity maps. 
2. `offset_tracking.py` - Runs the functions. 
3. `config.py` - Contains parameters which may be changed. 

### Functions:

**1. make_image_pair**: Takes two paths to images and creates a new folder in which to store processing files for other functions. It creates symbolic links to the original image paths and calculates the time interval between the two images.
   
**2. s1_slc_coreg**: Co-registers two images contained in a pair folder. This works by first calculating a rough initial offset between the two images, then determining a more precise offset polynomial using intensity cross-correlation using large window sizes. This offset information is stored in the OFF_par file. This function also resamples the secondary image (SLC2) onto the primary image.
   
**3. s1_slc_pwr_tracking**: Performs feature tracking. Currently, there is only one iteration of offset_pwr_tracking, as I'm not sure how it will work with previous offsets in the co-registration function. It then converts to a displacement map, converts to m/day, extracts velocity magnitude, and creates images of outputs.

**4. s1_vel_geocoding**: Converts velocity from slant range to ground range and creates a GeoTIFF. 

## Future Work
Future versions will improve system compatibility and extend setup for more types of imagery beyond Sentinel-1 SLCs
   
