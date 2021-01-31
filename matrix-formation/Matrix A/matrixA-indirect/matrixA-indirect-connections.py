import pandas as pd 
from tqdm.auto import tqdm


matrixA = pd.read_csv('matrixA.csv', header = 0 , index_col = None , sep =',') 
matrixB = pd.read_csv('symmetric_matrixB_indirect.csv', header = 0 , index_col = 0 , sep = ',') 
#the file is loaded here is an updated file by using the code in quotes, this file is different from the file that was obtained
#in the file ds_indirect.py


matrixA.set_index("zipcode", inplace = True)





'''
This part of code was used to check whether there were any common rows and columns for matrixB(ds_indirect.csv file)
if there were any then connections were cross checked if there is an already existing row then 
it will be updated with 1 if there was zero
or a new row or column will be added accordingly 
'''
'''
row = list(matrixB.index)
column = list(matrixB.columns)


def getConnectionRow(substation):
	column_connection = []
	count = 0
	for i in matrixB.loc[substation]:
		if i == 1.0:
			column_connection.append(column[count])
	count+=1
	return column_connection

def getConnectionColumn(substation):
	row_connection =[]
	count = 0
	for i in matrixB[substation]:
		if i == 1.0:
			row_connection.append(row[count])
	count +=1
	return row_connection 


for i in matrixB.index:
	if i in column:
		print(i)
		column_connection = getConnectionRow(i) #the row element is connected to which columns
		print(column_connection)
		row_connection = getConnectionColumn(i) # the column element is connected to which rows
		print(row_connection)
		for j in column_connection:
			if  not ( j in column) :
				#print(matrixB.loc[i,j]) 
				print(" New row has to be added")
				matrixB.loc[j,i] = 1
				#print(matrixB.loc[i,j])
			else:
				#print(matrixB.loc[i,j])
				print("already updating the existing row")
				matrixB.loc[j,i] = 1
				#print(matrixB.loc[i,j])
		for k in row_connection:
			if not ( k in row):
				#print(matrixB.loc[k,i])
				print(" New column has to be added ")
				matrixB.loc[i,k] = 1
				#print(matrixB.loc[k,i]) 
			else:
				#rint(matrixB.loc[k,i])
				print("already updating the existing column")
				matrixB.loc[i,k] = 1
				#print(matrixB.loc[k,i])
	else:
		pass


#matrixB.fillna(0,inplace = True)
#matrixB.to_csv('ds_indirect.csv')
'''

'''
count = 0

l = 0 
m = 0 
column = list(matrixB.columns)
for i in matrixB.loc["Groß Köris"]:
	if i == 1.0:
		print("Groß Köris is connected to " + column[count])
		l +=1
	count +=1

for i in matrixB.index:
	if matrixB.loc[i,"Groß Köris"] == 1.0:
		print(" Groß Köris is connected to " + i )
		m += 1

if l == m:
	print("voila You have done it")
else :
	print("you okay dude")


'''

matrixA_columns = list(matrixA.columns)
matrixA_rows = list(matrixA.index)

matrixB_columns = list(matrixB.columns)
matrixB_rows = list(matrixB.index)

#print(matrixB_columns) 
def getZipcodeConnection(substation):
	count = 0
	for i in matrixA.loc[substation]:
		if i == 1.0:
			return matrixA_columns[count]
		count += 1

def getIndirectConnection(substation):
	count = 0
	connection = [] 
	try:	
		for i in matrixB.loc[substation]:
			if i == 1.0:
				connection.append(matrixB_columns[count])
			count += 1
		return connection
	except KeyError:
		return connection




matrixA_indirect = pd.DataFrame(columns = matrixB_columns)

print('Creating a dummy matrixA with the same number of columns as matrixB')
for m in tqdm(matrixA_rows):
	matrixA_indirect.loc[m] = 0

matrixA_indirect.reindex(matrixA_rows)

print('updating the matrixA with the indirect connections')

keyerror = 0 
for i in tqdm(matrixA.index):
	zipcode_connection = getIndirectConnection(getZipcodeConnection(i))
	if zipcode_connection != []:
		for j in zipcode_connection:
			matrixA_indirect.loc[i,j] = 1.0
	else:
		keyerror += 1

print('there is KeyError '+ str(keyerror) + ' number of times')
print(matrixA_indirect)
matrixA_indirect.to_csv('matrixA_indirect.csv')






