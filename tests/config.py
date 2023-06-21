import os

class Config:
    
    test = 'Hello World again'
    
    
    PROJECT_DIR = '/nfs/a285/homes/gyjai/coding_projects/comparing_sar_vel/'
    IMAGE_DIR = 'data/images/s1/' 
    
    IMAGE_A_NAME = 'S1A_IW_20210702_125716_038599'
    IMAGE_B_NAME = 'S1A_IW_20210714_125717_038774'
    
    IMAGE_A_PATH = os.path.join(PROJECT_DIR, IMAGE_DIR, IMAGE_A_NAME)
    IMAGE_B_PATH = os.path.join(PROJECT_DIR, IMAGE_DIR, IMAGE_B_NAME)

    
    
    

    
    
   