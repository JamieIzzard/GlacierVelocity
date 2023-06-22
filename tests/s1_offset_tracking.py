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
    
    #proc.make_image_pair(Config.IMAGE_A_PATH, Config.IMAGE_B_PATH)
    
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
    
    

    # ... function body ...

if __name__ == "__main__":
    
    base_path = '/nfs/a285/homes/gyjai/coding_projects/comparing_sar_vel/tests/data/pairs/'
    image_folders = ['S1A_IW_20210702_125716_038599__S1A_IW_20210714_125717_038774']  # your actual folder names here



    
    for pair in image_folders:
        
        
        parts = pair.split("__")  # This will split the string into two parts
        image_A = parts[0]  # This is the part before the "__"
        image_B = parts[1]  # This is the part after the "__"
        
        print("Image A: ", image_A)
        print("Image B: ", image_B)
        
    
        SLC1 = os.path.join(base_path, pair, image_A, f'{image_A}.slc')
        SLC2 = os.path.join(base_path, pair, image_B, f'{image_B}.slc')
    
        SLC1_par = os.path.join(base_path, pair, image_A, f'{image_A}.slc_par')
        SLC2_par = os.path.join(base_path, pair, image_B, f'{image_B}.slc_par')
    
        COREG_SLC2 = os.path.join(base_path, pair, f'{pair}.COREG_SLC2.slc')
        COREG_SLC2_par = os.path.join(base_path, pair, f'{pair}.COREG_SLC2.par')
    
        OFF_par = os.path.join(base_path, pair, f'{pair}.OFF.par')
        offs = os.path.join(base_path, pair, f'{pair}.offs')
        ccp = os.path.join(base_path, pair, f'{pair}.ccp')
        offsets_txt = os.path.join(base_path, pair, f'{pair}.offsets.txt')
        coffs = os.path.join(base_path, pair, f'{pair}.coffs')
    
        slc1_bmp = os.path.join(base_path, pair, image_A, f'{image_A}.SLC1.bmp')
        coreg_slc_bmp = os.path.join(base_path, pair, f'{pair}.COREG_SLC2.bmp')
        
        print('Copying Scripts to Output Directory ')
        # Copy the scripts to the target folder
        shutil.copy('s1_offset_tracking.py', os.path.join(base_path, pair))  
        shutil.copy('config.py', os.path.join(base_path, pair))
        shutil.copy('processing.py', os.path.join(base_path, pair))

        
        main(SLC1, SLC2, SLC1_par, SLC2_par, COREG_SLC2, COREG_SLC2_par,
             OFF_par, offs, ccp, offsets_txt, coffs, slc1_bmp, coreg_slc_bmp)

        