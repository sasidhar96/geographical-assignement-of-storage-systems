import pandas as pd 
from tqdm.auto import tqdm
import numpy as np 

dstods_df = pd.read_csv('DS_to_DS.csv', header = 0, index_col = None , sep = ',')

dummy_df1 = dstods_df.loc[:,['Start']].drop_duplicates(subset = "Start").set_index('Start')
dummy_df2 = list(set(list(dstods_df["Ende"])))


matrix = pd.DataFrame(dummy_df1, columns = dummy_df2)


for i in tqdm(matrix.index):
	for j in dstods_df.index:
		if i == dstods_df.loc[j,'Start'] :
			matrix.loc[i,dstods_df.loc[j,'Ende']] = 1

matrix.fillna(0, inplace = True)

column = list(matrix.columns)

matrix.set_index('Start', inplace = True)

ds = list(set(list(matrix.index) + list(matrix.columns)))

symmetric_matrixB = pd.DataFrame(columns = ds)

for i in tqdm(ds):
	symmetric_matrixB.loc[i] = 0

def get_connection(substation):
	connection = []
	count = 0 
	for i in matrix.loc[substation]:
		if i == 1.0:
			connection.append(column[count])
		count += 1
	#print(connection)
	return connection


for i in tqdm(matrix.index):
	connection = get_connection(i)
	for j in connection:
		symmetric_matrixB.loc[i,j] = 1.0
		symmetric_matrixB.loc[j,i] = 1.0
	

symmetric_matrixB.to_csv('symmetric_matrixB.csv')