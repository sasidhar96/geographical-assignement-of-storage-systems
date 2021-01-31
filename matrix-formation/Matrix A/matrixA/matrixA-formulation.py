import pandas as pd 
import numpy as np 
from tqdm.auto import tqdm 

dstozipcodes = pd.read_csv('filtered_storageSystems_mapped.csv', header = 0 ,index_col = None, sep = ',')


new_df = dstozipcodes.drop_duplicates(subset="zipcode")
matrix_df = new_df.loc[:,['zipcode','UW']].set_index('zipcode')
#matrix_df.to_csv() 
#print(matrix_df)


substations = list(set(list(matrix_df['UW']))) #unique distributes substations

matrix = pd.DataFrame(matrix_df, columns = substations)
#print(matrix)


for i in tqdm(matrix.index):
	#print(i)
	for j in matrix_df.index:
		if i == j:
			#print(j)
			#print(matrix_df.loc[j,'UW'])
			#print(matrix.loc[i,matrix_df.loc[j,'UW']])
			#print('found match and updating the dataframe for the index '+ str(i) + ' at location ' + str(matrix.loc[i,matrix_df.loc[j,'UW']] ))
			matrix.loc[i,matrix_df.loc[j,'UW']] = 1.0
			#print(matrix.loc[i,matrix_df.loc[j,'UW']])
		#else:
		#	matrix.loc[i,matrix_df.loc[j,'UW']] = 0

matrix.fillna(0,inplace = True)
#print(matrix)	
matrix.to_csv('matrixA.csv')


