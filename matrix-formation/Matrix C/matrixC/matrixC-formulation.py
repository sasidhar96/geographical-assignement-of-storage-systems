import pandas as pd 
from tqdm.auto import tqdm
import numpy as np 

dstotl_df = pd.read_csv('updated_geocoded_50hztl.csv', header = 0, index_col = None , sep = ',')

dummy_df1 = dstotl_df.loc[:,['Start']].drop_duplicates(subset = "Start").set_index('Start')
dummy_df2 = list(set(list(dstotl_df["Ende"])))


matrix = pd.DataFrame(dummy_df1, columns = dummy_df2)


for i in tqdm(matrix.index):
	#print(i)
	for j in dstotl_df.index:
		#print(j)
		if i == dstotl_df.loc[j,'Start'] :
			#print("Found match")
			matrix.loc[i,dstotl_df.loc[j,'Ende']] = 1

matrix.fillna(0, inplace = True)
matrix.to_csv('matrixC.csv')