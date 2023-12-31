#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:16:12 2023

@author: gyjai
"""

from config import Config
import processing as proc
import os
import shutil




def main(SLC1, SLC2, SLC1_par, SLC2_par, COREG_SLC2, COREG_SLC2_par, 
         OFF_par, offs, ccp, offsets_txt, coffs, slc1_bmp, coreg_slc_bmp):
            
    proc.f_testing(Config.test)
    
    
    proc.make_image_pair(Config.IMAGE_A_PATH, Config.IMAGE_B_PATH, pair_directory)
    
    print('Coregistering Images')
    
    
    proc.s1_slc_coreg(SLC1, SLC2,
                      SLC1_par, SLC2_par,
                      OFF_par,
                      Config.rlks, Config.azlks,
                      Config.rwin_01, Config.azwin_01,
                      Config.rwin_02, Config.azwin_02,
                      offs, ccp,
                      offsets_txt,
                      Config.n_ovr,
                      Config.thres,
                      Config.lanczos,
                      Config.bw_frac,
                      coffs,
                      COREG_SLC2,
                      COREG_SLC2_par,
                      slc1_bmp,
                      coreg_slc_bmp)
    
    
    proc.s1_mli_geocoding(SLC1, SLC1_par, MLI1, MLI1_par, Config.dem_par, Config.dem, Config.dem_seg_par,
                          dem_seg, mli_lut1, mli_geo1, mli_geo_bmp1, mli_tif1)
    
    proc.s1_mli_geocoding(SLC2, SLC2_par, MLI2, MLI2_par, Config.dem_par, Config.dem, Config.dem_seg_par,
                          dem_seg, mli_lut2, mli_geo2, mli_geo_bmp2, mli_tif2)
    
    
    
    proc.s1_slc_pwr_tracking(SLC1, 
                    SLC2, 
                    SLC1_par, 
                    SLC2_par, 
                    OFF_par, 
                    pt1_offs, 
                    pt1_ccp, 
                    Config.pt1_rwin, 
                    Config.pt1_azwin, 
                    Config.pt1_novr, 
                    Config.pt1_thres, 
                    Config.pt1_rstep, 
                    Config.pt1_azstep, 
                    Config.pt_lanczos, 
                    Config.pt_bw_frac, 
                    pt1_disp, 
                    pt1_disp_bmp,
                    Config.interval, 
                    pt1_gnd,
                    pt1_real_off,
                    pt1_ccp_bmp,
                    pt1_vel_bmp)
    
    proc.s1_vel_geocoding(SLC2_par,
                         OFF_par,
                         Config.dem_par,
                         Config.dem,
                         Config.dem_seg_par,
                         dem_seg,
                         geo_lut,
                         pt1_real_off,
                         vel_geo,
                         vel_tif)
    
    
    
    
    
    
    

    # ... function body ...

if __name__ == "__main__":
    
    base_path = '/nfs/a285/homes/gyjai/coding_projects/comparing_sar_vel/tests/data/pairs/'
    
    '''
    pair_common = (f"{Config.IMAGE_A_NAME}__{Config.IMAGE_B_NAME}__"
           f"{Config.rwin_01}_{Config.azwin_01}_{Config.rwin_02}_{Config.azwin_02}_"
           f"{Config.pt1_rwin}_{Config.pt1_azwin}")
    
    '''
    
    pair_common = (f"{Config.IMAGE_A_NAME}__{Config.IMAGE_B_NAME}__testing_mli")
           
    
    

    pair_name = pair_common
    pair_directory = f"data/pairs/{pair_common}"

    image_folders = [pair_common] 

    for pair in image_folders:
        
        print(pair)
        
        
        os.makedirs(pair_directory, exist_ok=True)
        print('Pair directory created:', pair_directory)
        
        parts = pair.split("__")  # This will split the string into two parts
        image_A = parts[0]  # This is the part before the "__"
        image_B = parts[1]  # This is the part after the "__"
        
        print("Image A: ", image_A)
        print("Image B: ", image_B)
        
        #COREGISTRATION 
    
        # Input Files
        SLC1 = os.path.join(base_path, pair, image_A, f'{image_A}.baltoro_slc')
        SLC2 = os.path.join(base_path, pair, image_B, f'{image_B}.baltoro_slc')
    
        SLC1_par = os.path.join(base_path, pair, image_A, f'{image_A}.baltoro_slc_par')
        SLC2_par = os.path.join(base_path, pair, image_B, f'{image_B}.baltoro_slc_par')
        
    
        #Output Files
        COREG_SLC2 = os.path.join(base_path, pair, f'{pair}.COREG_SLC2.slc')
        COREG_SLC2_par = os.path.join(base_path, pair, f'{pair}.COREG_SLC2.par')
    
        OFF_par = os.path.join(base_path, pair, f'{pair}.off.par')
        offs = os.path.join(base_path, pair, f'{pair}.offs')
        ccp = os.path.join(base_path, pair, f'{pair}.ccp')
        offsets_txt = os.path.join(base_path, pair, f'{pair}.offsets.txt')
        coffs = os.path.join(base_path, pair, f'{pair}.coffs')
    
        slc1_bmp = os.path.join(base_path, pair, f'{pair}.SLC1.bmp')
        coreg_slc_bmp = os.path.join(base_path, pair, f'{pair}.COREG_SLC2.bmp')
        
        #MLIs
        
        MLI1 = os.path.join(base_path, pair, f'{image_A}.baltoro_mli')
        MLI2 = os.path.join(base_path, pair, f'{image_B}.baltoro_mli')

        MLI1_par = os.path.join(base_path, pair, f'{image_A}.baltoro_mli_par')
        MLI2_par = os.path.join(base_path, pair, f'{image_B}.baltoro_mli_par')
        
        mli_lut1 = os.path.join(base_path, pair, f'{image_A}.baltoro_mli_lut')
        mli_lut2 = os.path.join(base_path, pair, f'{image_B}.baltoro_mli_lut')
        
        mli_geo1 = os.path.join(base_path, pair, f'{image_A}.baltoro_mli_geo')
        mli_geo2 = os.path.join(base_path, pair, f'{image_B}.baltoro_mli_geo')
                            
        mli_geo_bmp1 = os.path.join(base_path, pair, f'{image_A}.baltoro_mli_geo.bmp')
        mli_geo_bmp2 = os.path.join(base_path, pair, f'{image_B}.baltoro_mli_geo.bmp')
        
        mli_tif1 = os.path.join(base_path, pair, f'{image_A}.baltoro_mli_geo.tif')
        mli_tif2 = os.path.join(base_path, pair, f'{image_B}.baltoro_mli_geo.tif')
        
        
        
        #OFFSET TRACKING
        
        # Output Files
        
        pt1_offs = os.path.join(base_path, pair, f'{pair}.pt1.offs')
        pt1_ccp = os.path.join(base_path, pair, f'{pair}.pt1.ccp')
        pt1_disp = os.path.join(base_path, pair, f'{pair}.pt1.disp')
        pt1_disp_bmp = os.path.join(base_path, pair, f'{pair}.pt1_disp.bmp')
        
        pt1_gnd = os.path.join(base_path, pair, f'{pair}.pt1.gnd')
        pt1_real_off = os.path.join(base_path, pair, f'{pair}.pt1.real_off')
        pt1_ccp_bmp = os.path.join(base_path, pair, f'{pair}.pt1.ccp.bmp')
        pt1_vel_bmp = os.path.join(base_path, pair, f'{pair}.pt1.vel.bmp')
        
        
        # Geocoding Velocity
    
        dem_seg = os.path.join(base_path, pair, f'{pair}.dem_seg')
        geo_lut = os.path.join(base_path, pair, f'{pair}.geo.lut')
        vel_geo = os.path.join(base_path, pair, f'{pair}.pt1.vel.geo')
        vel_tif = os.path.join(base_path, pair, f'{pair}.pt1.vel.geo.tif')
        
        
        files = [
            COREG_SLC2,
            COREG_SLC2_par,
            OFF_par,
            offs,
            ccp,
            offsets_txt,
            coffs,
            slc1_bmp,
            coreg_slc_bmp,
            pt1_offs,
            pt1_ccp,
            pt1_disp,
            pt1_disp_bmp,
            dem_seg
        ]
        
        
        for file in files:
            if os.path.exists(file):
                os.remove(file)
                print(f'File {file} has been deleted.')
            else:
                print(f'File {file} does not exist.')
        
        
        print('Copying Scripts to Output Directory ')
        # Copy the scripts to the target folder
        shutil.copy('s1_offset_tracking.py', os.path.join(base_path, pair))  
        shutil.copy('config.py', os.path.join(base_path, pair))
        shutil.copy('processing.py', os.path.join(base_path, pair))

        
        main(SLC1, SLC2, SLC1_par, SLC2_par, COREG_SLC2, COREG_SLC2_par,
             OFF_par, offs, ccp, offsets_txt, coffs, slc1_bmp, coreg_slc_bmp)

        