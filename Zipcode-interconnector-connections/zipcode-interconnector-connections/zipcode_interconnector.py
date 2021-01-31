import pandas as pd 
from tqdm.auto import tqdm


matrixA = pd.read_csv('matrixA_indirect.csv', header = 0 , index_col = 0 , sep = ',')


rowA = list(matrixA.index)
columnA = list(matrixA.columns) 

matrixC = pd.read_csv('matrixC_indirect_connection.csv', header = 0 , index_col = 0 , sep = ',')

rowC = list(matrixC.index)
columnC = list(matrixC.columns)

'''
the created dataframe is converted to csv file that can be loaded whenever required
zipcodeinterconnector = pd.DataFrame(rowA,columns = columnC)
for i in tqdm(rowA):

	zipcodeinterconnector = zipcodeinterconnector.append([i])

print(zipcodeinterconnector.index)
print(zipcodeinterconnector.columns)
zipcodeinterconnector.to_csv('zipcodeinterconnector.csv', index = False )

''' 

matrixA_C = pd.DataFrame(columns = columnC)
print('creating a dummy matrix ...')
for m in tqdm(rowA):
	matrixA_C.loc[m] = 0



def getDsTlConnection(interconnector):
	connection = []
	count = 0
	for i in matrixC[interconnector]:
		if i == 1.0:
			connection.append(rowC[count])
		count += 1
	return connection 

def getZipcodeConnection(substation):
	connection = []
	count = 0
	try:
		for i in matrixA[substation]:
			if i == 1.0:
				connection.append(rowA[count])
			count += 1
		return connection

	except KeyError:
		print('No zipcodes are connected to the ' + substation)
		return [' ']



for i in tqdm(columnC):
	print('updating the interconnector column :' + i + ' ....')
	connection = getDsTlConnection(i)
	#print( i + ' interconnector is connected to the distributed substations '+ str(connection))
	#count = 0 
	for j in tqdm(connection):
		zipcode_connection = getZipcodeConnection(j)
		#print('updating the zipcodes connected to '+ str(count) + ' DS')
		#count += 1
		for k in zipcode_connection:
			matrixA_C.loc[k,i] = 1.0
			#print("updated the matrix for the zipcode "+ str(k))

	#print("updating the zipcode affecting the interconnector " + i + " in the matrix")


#zipcodeinterconnector.fillna(0,inplace = True)
matrixA_C.to_csv('zipcode_interconnector_connection.csv')


