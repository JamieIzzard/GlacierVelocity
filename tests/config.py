import os

class Config:
    
    test = 'Hello World again'
    
    ### INDIVIDUAL IMAGES PATHS FOR FINDING PAIRS
    
    
    PROJECT_DIR = '/nfs/a285/homes/gyjai/coding_projects/comparing_sar_vel/'
    IMAGE_DIR = 'data/images/s1/' 
    
    IMAGE_A_NAME = 'S1A_IW_20210702_125716_038599'
    IMAGE_B_NAME = 'S1A_IW_20210726_125718_038949'
    
    IMAGE_A_PATH = os.path.join(PROJECT_DIR, IMAGE_DIR, IMAGE_A_NAME)
    IMAGE_B_PATH = os.path.join(PROJECT_DIR, IMAGE_DIR, IMAGE_B_NAME)
    
    
    #DEMS
    
    dem_par = '/nfs/a285/homes/gyjai/dems/baltoro_cop30.dem_par'
    dem = '/nfs/a285/homes/gyjai/dems/baltoro_cop30.dem'
    
    dem_seg_par = '/nfs/a285/homes/gyjai/dems/baltoro_10.dem_seg_par'


    # COREGISTRATION PARAMETERS
    
    rlks = 32         # These Should be Same as Step Size in Feature Tracking
    azlks = 8       #
    
    rwin_01 = 512      # Range Window Size for Initial Offset determination
    azwin_01 = 128    # Azimuth Window Size for Initial Offset determination
    
    
    #Parameters for offset_pwr
    
    rwin_02 = 1028     #
    azwin_02 = 256     #
    n_ovr = 1     #
    thres = 0.1        # 
    lanczos = 5      #
    bw_frac = 1      #
    
    #Parameters for Offset_pwr_tracking
    
    pt1_rwin = 512
    pt1_azwin = 128
    pt1_novr = 1
    pt1_thres = 0.1
    pt1_rstep = 32
    pt1_azstep = 8
    pt_lanczos = 5
    pt_bw_frac = 1.0
    
    #
    interval = 0.041667

    
    
    

    
    
   