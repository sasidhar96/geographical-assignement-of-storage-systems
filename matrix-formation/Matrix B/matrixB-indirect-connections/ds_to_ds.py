import pandas as pd 
from tqdm.auto import tqdm
import numpy as np 

matrix2 = pd.read_csv('symmetric_matrixB.csv',header = 0, index_col = 0 , sep = ',')
#print(matrix2)
indirect_connection = 1 

column = list (matrix2.columns)

def getPrimaryConnection(substation):
	''' 
	This function takes the row in which we want to find the primary connection as an input 
	and returns the column names in which there are ones implying that 
	there is a connection between row and column in the form of a list
	'''
	count = 0 
	primary_connection = []
	for i in matrix2.loc[substation]:
		if i == 1.0:
				#print("connection found at index location " + str(count))
				#print(matrix2.loc["Baruth", column[count]])
				#print(column[count])
			primary_connection.append(column[count])
		count += 1
	return primary_connection

def getIndirectConnection(substation):
	count = 0
	secondary_connection1 = []
	#print(substation)
	#print(secondary_connection1)
	#print(substation + str(secondary_connection))
	#print('getting indirect connection....')
	for j in matrix2.loc[substation]:
		if j == 1.0:
			secondary_connection1.append(column[count])
		count +=1 
	return secondary_connection1

def getIndirectConnection2(substation):
	count = 0
	secondary_connection1 = []
	#print(substation)
	#print(secondary_connection1)
	#print(substation + str(secondary_connection))
	#print('getting indirect connection....')
	for j in matrix2.loc[substation]:
		if j == 1.0:
			secondary_connection1.append(column[count])
		count +=1 
	return secondary_connection1


def cell():
	for i in tqdm(matrix2.index):

		primary_connection = getPrimaryConnection(i)

		#print(str(i) +' is directly connected to ' + str(primary_connection) )

		for j in primary_connection:
			#print(j)
			secondary_connection = [' ']
			secondary_connection = getIndirectConnection(j)
			for k in secondary_connection:
				if k!= ' ':
					matrix2.loc[i,k] = indirect_connection
					matrix2.loc[k,i] = indirect_connection
					secondary_connection2 = getIndirectConnection(k)
					#print(k + ' is connected to '+ str(secondary_connection1))
					for l in secondary_connection2:
						if l in secondary_connection:
							pass
						else:
							secondary_connection.append(l)
						
				else:
					pass
			#print(dummy)
			#print(str(2) + j)
			#secondary_connection.append(" ")
			#print(secondary_connection)
			'''
			for k in secondary_connection :
				if k!= ' ':
					matrix2.loc[i,k] = indirect_connection
					matrix2.loc[k,i] = indirect_connection
					secondary_connection = getIndirectConnection(k, secondary_connection)
					#print(str(3)+ k )
				else :
					pass
			'''
		

	matrix2.to_csv('symmetric_matrixB_indirect.csv')


cell()