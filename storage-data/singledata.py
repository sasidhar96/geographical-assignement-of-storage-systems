# code to concatenate multiple csv files into a single csv file 

import glob 
import pandas as pd 


extension = 'csv'

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f, error_bad_lines = False) for f in all_filenames])

combined_csv.to_csv("conbined_csv.csv",index = False)