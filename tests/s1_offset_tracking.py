#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:16:12 2023

@author: gyjai
"""

from config import Config
import processing as proc

def main():
    
    proc.f_testing(Config.test)
    
    
    #proc.make_image_pair(Config.IMAGE_A_PATH, Config.IMAGE_B_PATH)
    
    
    proc.s1_slc_coreg(SLC1, SLC2,
                      SLC1_par, SLC2_par,
                      OFF_par,
                      config.rlks, config.azlks,
                      config.rwin_01, config.azwin_01,
                      config.rwin_01, config.azwin_01,
                      offs, ccp,
                      offsets_txt,
                      config.n_ovr,
                      config.nr, config.naz,
                      config.thres,
                      config.lanczos,
                      config.bw_frac,
                      COREG_SLC2,
                      COREG_SLC2_par)
    
    
if __name__ == "__main__":
    main()