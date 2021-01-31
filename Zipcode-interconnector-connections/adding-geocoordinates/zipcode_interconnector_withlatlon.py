import pandas as pd 
from tqdm.auto import tqdm 


zipcode_interconnector = pd.read_csv('zipcode_interconnector_connection.csv' , header = 0, index_col = 0, sep = ',')

zipcode_coordinates = pd.read_csv('filtered_storageSystems_mapped.csv', header = 0 ,index_col = None, sep = ',')

interconnector_coordinates = pd.read_csv('updated_geocoded_50hztl.csv', header = 0 , index_col = None, sep = ',')

zipcode_coordinates = zipcode_coordinates.loc[:,['zipcode','lat', 'lon']]
zipcode_coordinates = zipcode_coordinates.drop_duplicates(subset = ['zipcode'])
zipcode_coordinates.set_index("zipcode", inplace = True)

interconnector_coordinates = interconnector_coordinates.loc[:,['Ende','end_lat','end_lon']]
interconnector_coordinates = interconnector_coordinates.drop_duplicates(subset = ['Ende'])
interconnector_coordinates.set_index('Ende', inplace = True)

'''
def getZipcodeCoordinates(zipcode):
	for i in zipcode_coordinates.index:
		if i == zipcode:
			print('found match')

			#print('coordinates are ' + str(zipcode_coordinates.loc[i,'lat']) + ','+ str(zipcode_coordinates.loc[i,'lon']))
			return (zipcode_coordinates.loc[i,'lat'],zipcode_coordinates.loc[i,'lon'])

'''
#print(str(zipcode_coordinates.loc[19348,'lat']) + ','+ str(zipcode_coordinates.loc[19348,'lon']))
#zipcode_interconnector.loc[19348,'latitude of zipcode'],zipcode_interconnector.loc[19348,'longitude of zipcode'] = zipcode_coordinates.loc[19348,'lat'],zipcode_coordinates.loc[19348,'lon']

#zipcode_interconnector.loc[19348,'latitude of zipcode'] = zipcode_coordinates.loc[19348,'lat']

#print(zipcode_interconnector)

print('updating the geo-coordinates of zipcodes ')
for i in tqdm(zipcode_interconnector.index):
	try:
		temp = float(i)
		zipcode_interconnector.loc[i,'latitude of zipcode'],zipcode_interconnector.loc[i,'longitude of zipcode'] = zipcode_coordinates.loc[temp,'lat'],zipcode_coordinates.loc[temp,'lon']
	except ValueError:
		print(i)


print('updated the geo-coordinates of zipcodes ')


def getInterconnectorCoordinates(interconnector):
	for i in interconnector_coordinates.index:
		if i == interconnector:
			return interconnector_coordinates.loc[i,'end_lat'], interconnector_coordinates.loc[i,'end_lon']
	return 0,0


column = list(zipcode_interconnector.columns)
df1 = pd.DataFrame(columns = column).reindex(['latitude of interconnector'])
zipcode_interconnector = zipcode_interconnector.append(df1)

df2 = pd.DataFrame(columns = column).reindex(['longitude of interconnector'])
zipcode_interconnector = zipcode_interconnector.append(df2)
print('updating the interconnector geo-coordinates')

for i in tqdm(column):
	zipcode_interconnector.loc['latitude of interconnector',i],zipcode_interconnector.loc['longitude of interconnector',i] = getInterconnectorCoordinates(i)

	#print(i + ' interconnector has latitude ' + str(lat) + " and longitude "+ str(lon))
	#print(i + " interconnector has latitude " + str(zipcode_interconnector[index1,i]) + " and longitude " + str(zipcode_interconnector[index2,i]))


print('updated the interconnector geo-coordinates')

zipcode_interconnector.fillna(0,inplace = True)
zipcode_interconnector.to_csv('zipcode_interconnector_withlatlon.csv')
