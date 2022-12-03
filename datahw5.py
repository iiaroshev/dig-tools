#from homework 5

import pandas as pd
import numpy as np
import h5py 
import time

df = pd.DataFrame(np.random.randn(10**6, 4), columns=list('xycv'))
df['y'] = df['c']

time_req = open('times_req.txt', 'w')

feather_start = time.time()   

df.to_feather('Feather')

feather_end = time.time()

time_req.write("Time spent to Feather file: " + str(feather_end-feather_start) + " seconds " + '\n')

hdf_start = time.time()    

df.to_hdf('HDF', key = 'df')

hdf_end = time.time()

time_req.write("Time spent to HDF file: " + str(hdf_end-hdf_start) + " seconds " + '\n')

parquet_start = time.time() 

df.to_parquet('Parquet')

parquet_end = time.time()

time_req.write("Time spent to Parquet file: " + str(parquet_end-parquet_start) + " seconds " + '\n')

readFrame = pd.read_feather('Feather', columns=None, use_threads=True)  #last task
print(readFrame)
