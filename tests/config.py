import os

class Config:
    
    test = 'Hello World again'
    
    ### INDIVIDUAL IMAGES PATHS FOR FINDING PAIRS
    
    
    PROJECT_DIR = '/nfs/a285/homes/gyjai/coding_projects/comparing_sar_vel/'
    IMAGE_DIR = 'data/images/s1/' 
    
    IMAGE_A_NAME = 'S1A_IW_20210702_125716_038599'
    IMAGE_B_NAME = 'S1A_IW_20210714_125717_038774'
    
    IMAGE_A_PATH = os.path.join(PROJECT_DIR, IMAGE_DIR, IMAGE_A_NAME)
    IMAGE_B_PATH = os.path.join(PROJECT_DIR, IMAGE_DIR, IMAGE_B_NAME)


    # COREGISTRATION PARAMETERS
    
    rlks = 128         # These Should be Same as Step Size in Feature Tracking
    azlks = 32       #
    
    rwin_01 = 1028      # Range Window Size for Initial Offset determination
    azwin_01 = 256    # Azimuth Window Size for Initial Offset determination
    
    
    #Parameters for offset_pwr
    
    rwin_02 = 256      #
    azwin_02 = 64     #
    n_ovr = 2       #
    
    thres = 0.1        # 
    lanczos = 5      #
    bw_frac = 1      #

    
    
    

    
    
   