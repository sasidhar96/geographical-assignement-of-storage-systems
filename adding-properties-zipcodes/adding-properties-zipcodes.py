#Code to calculate the number of storage systems, gross output, net nominal power
#of a single zipcode 


import pandas as pd 
import mysql.connector 
from tqdm.auto import tqdm
from collections import Counter

zipcode_df = pd.read_csv('geocoded_zipcode.csv', index_col = None, header = 0 , sep = ',')


#initialize new coulmns where you want to update the values from database 
zipcode_df['number of storage systems'] = 0
zipcode_df['number of solar modules'] = 0
zipcode_df['gross output'] = 0
zipcode_df['net nominal power'] = 0
zipcode_df['Solar energy storage'] = 0 
zipcode_df['Storage'] = 0
zipcode_df['Natural gas'] = 0
zipcode_df['Biomass'] = 0
zipcode_df['Wind'] = 0
zipcode_df['Water'] = 0 

mydb = mysql.connector.connect( host = 'localhost', user = 'root', password = 'priyareddy', database = 'storagedata')
mycursor = mydb.cursor() 

#converting the zipcode column to string from int 
for i in zipcode_df.index:
	zipcode_df.loc[i,'zipcode']  = str(zipcode_df.loc[i,'zipcode'])


ind = 0
for zip_code in tqdm(zipcode_df['zipcode']):

    #print('zipcode you want to search for is ' + zip_code)
    mycursor.execute('''SELECT COUNT(Plz),
    					SUM(Number_of_solarmodules),
    					SUM(Gross_output),
    					SUM(Net_nominal_output) 
    					FROM storage_data_base  
    					WHERE Plz = %s;''',(zip_code,))
    myresult = mycursor.fetchall()
    #for loop to update  the columns from the result from database
    for x,y,z,t in myresult:
        #print(' Number of storage systems at ' + str(zip_code) + ' are' + str(x) + ' and Gross output is '+ str(y) + ' and Net nominal power is ' + str(z) )
        zipcode_df.loc[ind,'number of storage systems'] = x
        zipcode_df.loc[ind,'number of solar modules'] = y
        zipcode_df.loc[ind,'gross output'] = z
        zipcode_df.loc[ind,'net nominal power'] = t
        #ind += 1


    mycursor.execute('''SELECT Storage_type FROM storage_data_base WHERE Plz = %s;''',(zip_code,))

    myresult = mycursor.fetchall()

    lst = []

    for x, in myresult:
    	lst.append(x)

    occurance = Counter(lst)

    if occurance['Solare Strahlungsenergie']> 0:
    	zipcode_df.loc[ind,'Solar energy storage'] = occurance['Solare Strahlungsenergie']

    if occurance['Speicher'] > 0:
    	zipcode_df.loc[ind,'Storage']  = occurance['Speicher']
    
    if occurance['Erdgas'] > 0 :
    	zipcode_df.loc[ind,'Natural gas'] = occurance['Erdgas']

    if occurance['Biomasse'] > 0 :
    	zipcode_df.loc[ind,'Biomass'] = occurance['Biomasse']

    if occurance['Wind'] > 0:
    	zipcode_df.loc[ind,'Wind'] = occurance['Wind']
    
    if occurance['Wasser'] > 0:
    	zipcode_df.loc[ind,'Water'] = occurance['Wasser']
    

    ind += 1


zipcode_df.to_csv('output_data.csv', index = False)