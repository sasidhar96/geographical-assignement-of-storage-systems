import pandas as pd 
from tqdm.auto import tqdm 



zipcode_interconnector = pd.read_csv('zipcode_interconnector_withlatlon.csv', header = 0 , index_col= 0, sep =',', low_memory = False)

properties = pd.read_csv('storagesystems_withnewGO.csv', header = 0 , index_col = None , sep =',')
properties = properties.drop(columns = ['loc_id','name','lat','lon','closest substation lat','closest substation lon','UW'])
properties = properties.drop_duplicates(subset = ['zipcode'])
properties.set_index("zipcode", inplace = True)




columnB = list(zipcode_interconnector)

def getProperty(zipcode):
	if zipcode != 'latitude of substation' and zipcode != 'longitude of substation':   #chnage the codition based on the df you are working
		for i in properties.index:
			if float(i) == float(zipcode):
				#print('Found a match ')
				return list(properties.loc[i]) #return the list with all the properties

	else:
		return []




def addProperty(zipcode, attribute ):
	count = 0
	for i in zipcode_interconnector.loc[zipcode]:
		
		if i == 1.0:
			zipcode_interconnector.loc[zipcode,columnB[count]] = attribute
		count += 1



for i in tqdm(zipcode_interconnector.index):
	try:
		zipcode_properties = getProperty(i)
	except ValueError:
		pass

	if zipcode_properties != []:
		addProperty(i,zipcode_properties[10]) 
	
	else:
		pass




zipcode_interconnector.to_csv('zipcode_interconnector_grossoutput.csv')
