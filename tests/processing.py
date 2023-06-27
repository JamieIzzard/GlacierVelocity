#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:06:52 2023

@author: gyjai

This is a new script to feature track S1 SLCs, as the old ones were getting very messy. 

This one uses more recent and advanced methods for co-registration and \
    feature tracking which should result in more accurate results.
"""


from datetime import datetime
import os
import py_gamma as pg

import sys
print(sys.version)

sys.path.insert(0, '/apps/applications/gamma/20221129/1/default/')


def f_testing(test_var):
    print(test_var)


viridis_cmap = '/nfs/a1/earmla/software/GAMMA/20221129/DISP/cmaps/viridis.cm'



def make_image_pair(IMAGE_A_PATH, IMAGE_B_PATH, pair_directory):
    
    print('making pair')
    
    # Verify source directory A
    if not os.path.isdir(IMAGE_A_PATH):
        print('Image directory not found:', IMAGE_A_PATH)
        print('Absolute path:', os.path.abspath(IMAGE_A_PATH))
        print('Current working directory:', os.getcwd())
        exit()
    
    print('Source directory A exists:', IMAGE_A_PATH)
    
    # Verify source directory B
    if not os.path.isdir(IMAGE_B_PATH):
        print('Image directory not found:', IMAGE_B_PATH)
        print('Absolute path:', os.path.abspath(IMAGE_B_PATH))
        print('Current working directory:', os.getcwd())
        exit()
    
    print('Source directory B exists:', IMAGE_B_PATH)
    
    # Calculate short names
    image_a_name = os.path.basename(IMAGE_A_PATH)
    image_b_name = os.path.basename(IMAGE_B_PATH)
    
    # Create new directory
    
    
    
    print('IMAGE_A_PATH=', IMAGE_A_PATH)
    print('')
    
    # Calculate the relative path from the symlink to the target file or directory
    relative_path_a = os.path.relpath(IMAGE_A_PATH, pair_directory)
    relative_path_b = os.path.relpath(IMAGE_B_PATH, pair_directory)
    
    # Create symbolic link for image A using the relative path
    link_path_a = os.path.join(pair_directory, image_a_name)
    if os.path.islink(link_path_a):
        os.unlink(link_path_a)
    os.symlink(relative_path_a, link_path_a)
    
    # Create symbolic link for image B using the relative path
    link_path_b = os.path.join(pair_directory, image_b_name)
    if os.path.islink(link_path_b):
        os.unlink(link_path_b)
    os.symlink(relative_path_b, link_path_b)


    

    
    # Calculate time difference
    date_format = "%Y%m%d%H%M%S"
    start_date_time_a = datetime.strptime(image_a_name.split('_')[2] + image_a_name.split('_')[3], date_format)
    start_date_time_b = datetime.strptime(image_b_name.split('_')[2] + image_b_name.split('_')[3], date_format)
    time_difference = abs(start_date_time_a - start_date_time_b)
    
    print(time_difference)




def s1_slc_coreg(SLC1, SLC2,
                 SLC1_par, SLC2_par,
                 OFF_par,
                 rlks, azlks,
                 rwin_01, azwin_01,
                 rwin_02, azwin_02,
                 offs, ccp,
                 offsets_txt,
                 n_ovr,
                 thres,
                 lanczos,
                 bw_frac,
                 coffs,
                 COREG_SLC2,
                 COREG_SLC2_par,
                 slc1_bmp,
                 coreg_slc_bmp):
    
    print(SLC1, SLC2, SLC1_par, SLC2_par, OFF_par, rlks, azlks,
          rwin_01, azwin_01, rwin_02, azwin_02, offs, ccp, offsets_txt,
          n_ovr, thres, lanczos, bw_frac, coffs, COREG_SLC2, COREG_SLC2_par, slc1_bmp, coreg_slc_bmp)
    
    '''
    ##These Three steps might not be necessary
    #Derive coreg Lookup Table
    #This might require DEM in RDC
    
    pg.rdc_trans()
    
    #Resample Image B into geometry of Image A
    pg.SLC_interp_lt()
    
    #Mask out moving objects
    pg.poly_mask()
    
    ############
    '''
    
    #Create offset parameter file for refinement of coregistration
    pg.create_offset(SLC1_par,    
                     SLC2_par,    
                     OFF_par,     
                     1,           
                     rlks,azlks, 
                     0)
                    

    #Deternine initial offsets
    pg.init_offset(SLC1,
                   SLC2,
                   SLC1_par,
                   SLC2_par,
                   OFF_par,
                   rlks,azlks,
                   '-','-', #Centre of Patch in Image Center
                   '-','-', #No Initial Offset
                   rwin_01,azwin_01, #Window size for Initial Offset Estimation (Default:512)
                   1,0) #Copy to Off_par, No Deramp
                   
                   
    
    #Determine offset polynomial using intensity cross correlation ()
    pg.offset_pwr(SLC1,
                  SLC2,
                  SLC1_par,
                  SLC2_par,
                  OFF_par,
                  offs,           #Output Offsets
                  ccp,
                  rwin_02,azwin_02,
                  offsets_txt,
                  n_ovr,
                  '-', '-',  #Numner of Offsets un Az R, default from off_par
                  thres,
                  lanczos,
                  bw_frac,
                  0,1,0,0) #No Deramp, Low Pass filter of Intensity, Print Summmary, No  pdf plot)
                  
                  
        
    
    #Fit Polynomial, this should should write polynomial to off file
    pg.offset_fit(offs,       #Input Offsets from Offset_pwr
                  ccp,        #Inout cross-correlation from offset_pwr
                  OFF_par,     #Both input and Output
                  coffs)      #Culled Offsets, fcomplex. Also Residuals? Need to Plot these
    
    
    #Resample Secondary SLC onto Primary using Offsets
    #There also exists SLC_interp_map which might be better for this
    pg.SLC_interp(SLC2,
                  SLC1_par,
                  SLC2_par,
                  OFF_par,
                  COREG_SLC2,
                  COREG_SLC2_par)
    
    slc1_params = pg.ParFile(SLC1_par)
    slc1_width = slc1_params.get_value('range_samples')
    
    print('SLC1 Width:', slc1_width,'\n')
    
    coreg_params = pg.ParFile(COREG_SLC2_par)
    coreg_width = coreg_params.get_value('range_samples')
    
    print('Coregistered SLC2 Width:', coreg_width,'\n')
    
    
    pg.rascpx(SLC1, 
              slc1_width,
              1, '-', '-', 20, 5,
              '-', '-', 'gray.cm', 
              slc1_bmp, 
              '-', '-', 0, '-')
    
    pg.rascpx(COREG_SLC2, 
              coreg_width,
              1, '-', '-', 20, 5,
              '-', '-', 'gray.cm', 
              coreg_slc_bmp, 
              '-', '-', 0, '-')
    


    
    #Need to Check the Following:
        #Should I be creating a new off_par file after Co-registration?
        #Is the offset_pwr in coreg equivalent to offset_pwr_tracking?
        
def s1_slc_pwr_tracking(SLC1: str, COREG_SLC2: str, SLC1_par: str, COREG_SLC2_par: str, OFF_par: str, pt1_offs: str,
                        pt1_ccp: str, pt1_rwin: int, pt1_azwin: int, pt1_novr: int, pt1_thres: float, pt1_rstep: int, 
                        pt1_azstep: int, pt_lanczos: int, pt_bw_frac: float, pt1_disp: str, pt1_disp_bmp: str,
                        interval: float, pt1_gnd: str, pt1_real_off: str, pt1_ccp_bmp: str, pt1_vel_bmp: str):
    
    # Initial Offset estimate with Very Large Window
    pg.offset_pwr_tracking(SLC1, COREG_SLC2, SLC1_par, COREG_SLC2_par, OFF_par, pt1_offs, pt1_ccp, pt1_rwin, 
                           pt1_azwin, '-', pt1_novr, pt1_thres, pt1_rstep, pt1_azstep, '-', '-', '-', '-', pt_lanczos, 
                           pt_bw_frac, 0, 1, 0, 0)
    
    # Convert Initial Offset Estimate to Displacement Map
    pg.offset_tracking(pt1_offs, pt1_ccp, SLC1_par, OFF_par, pt1_disp, '-', 2, '-', '-')
    
    params = pg.ParFile(OFF_par)
    pixels = params.get_value('offset_estimation_range_samples')
    
    
    pg.rascpx(pt1_disp, pixels, 0, '-', '-', '-', '-', '-','-','viridis.cm', pt1_disp_bmp)
    
    pg.lin_comb_cpx(1,pt1_disp,0,0,interval, 0,pt1_gnd,pixels,1,0,1,1,1)

    pg.cpx_to_real(pt1_gnd, pt1_real_off, pixels, 3)
    
    pg.ras_linear(pt1_ccp, pixels, cmap='cc.cm', rasf=pt1_ccp_bmp)
    
    pg.ras_linear(pt1_real_off, pixels, '-','-','-','-',0,1, '-','viridis.cm',pt1_vel_bmp)

    '''
    
    #Fill in gaps in inital estimate
    pg.interp_ad(offs,
                 interp_offs, 
        )
    
    #This time precise offsets
    pg.offset_pwr_tracking2(SLC1,
                            COREG_SLC2,
                            SLC1_par,
                            COREG_SLC2_par,
                            OFF_par,
                            pt2_offs,
                            pt2_ccp,
                            OFF_par2,
                            offs2,
                            pt2_rwin, pt2_azwin,
                            '-',
                            pt2_novr,
                            pt2_thres,
                            pt2_rstep, pt2_azstep,
                            '-','-','-','-',
                            pt2_bw_frac,
                            0,1,0,0)
        
    
    pg.offset_tracking()
    
    '''

def s1_vel_geocoding(COREG_SLC2_par: str, OFF_par: str, dem_par: str, dem: str, dem_seg_par: str, dem_seg: str,
                     geo_lut: str, real_off: str, vel_geo: str, vel_tif: str):
    
    pg.gc_map(COREG_SLC2_par,
              OFF_par,
              dem_par,
              dem,
              dem_seg_par,
              dem_seg,
              geo_lut)  
        

    dem_seg_par_obj = pg.ParFile(dem_seg_par)
    geocoded_width = dem_seg_par_obj.get_value('width', dtype=int)

    params = pg.ParFile(OFF_par)
    pixels = params.get_value('offset_estimation_range_samples')

    print(pixels, geocoded_width)
        
    pg.geocode_back(real_off,\
                    pixels,\
                    geo_lut,\
                    vel_geo,\
                    geocoded_width,\
                    '-',3,0)
        
    pg.data2geotiff(dem_seg_par, vel_geo, 2, vel_tif)
    
    '''
        
    pg.geocode_back(x_offs,\
                    pixels,\
                    geo_lut,\
                    x_geo,\
                    geocoded_width,\
                    '-',3,0)
    pg.geocode_back(y_offs,\
                    pixels,\
                    geo_lut,\
                    y_geo,\
                    geocoded_width,\
                    '-',3,0)
        
    pg.swap_bytes(x_geo, x_geo_swab,4)
    pg.swap_bytes(y_geo, y_geo_swab,4)

    pg.data2geotiff(dem_seg_par, x_geo, 2, x_tif)
    pg.data2geotiff(dem_seg_par, y_geo, 2, y_tif)
    
    '''
