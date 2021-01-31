import pandas as pd 
from tqdm.auto import tqdm


matrixB = pd.read_csv('symmetric_matrixB_indirect.csv', header = 0, index_col = 0 , sep = ',') #476*477
#print(matrixB)
#print(matrixB.shape)


matrixC = pd.read_csv("matrixC.csv", header = 0, sep = ',') #273*58
matrixC.set_index("Start",inplace = True)
#print(matrixC)
#print(matrixC.shape)


#It can concluded that there are no common substation hence we can concat the dataframes directly

columnB = list(matrixB.columns)
rowB = list(matrixB.index)

columnC = list(matrixC.columns)
rowC = list(matrixC.index)

#print(column.index("Sai"))


def getDirectConnection(substation):
	connection = []
	for i in matrixC.index:
		if matrixC.loc[i,substation] == 1.0:
			connection.append(i)
	return connection


'''
diff1 = set(columnB) & set(columnC)
diff2 = set(rowC) & set(rowB)  # there are common between these two 
diff3 = set(rowB) & set(columnC)
diff4 = set(rowC) & set(columnB) # there are common between these two 
print(diff1)
print(diff2)
print(diff3)
print(diff4)
'''

def getIndirectConnection(substation):
	connection = []
	if substation in rowB:
		#print("searching for connection between row and its columns")
		count = 0 
		for i in matrixB.loc[substation]:
			if i == 1.0:
				connection.append(columnB[count])
			count += 1
		return connection
	else:
		return [' ']


matrixC_indirect = pd.DataFrame(columns = columnC)


for m in rowB:
	matrixC_indirect.loc[m] = 0
matrixC_indirect.reindex(rowB)

for i in tqdm(columnC):
	#print(i)
	connection = getDirectConnection(i)
	#print( i + ' interconnector is connected to the substations ' + str(connection))
	for j in connection:
		if j != ' ':
			matrixC_indirect.loc[j,i] = 1.0
			connection2 = getIndirectConnection(j) #finding the connections of the substations directly connected 
			#to the substation connected to the interconnector
			for k in connection2:
				if k in connection:
					pass
				else:
					connection.append(k)
		else:
			pass

	#print(i + ' interconnector is conected to the substations ' + str(len(connection)))
matrixC_indirect.fillna(0, inplace = True)

matrixC_indirect.to_csv('matrixC_indirect_connection.csv')






