import pandas as pd 
import mysql.connector 
from tqdm.auto import tqdm

#df = pd.read_csv('single_data.csv', index_col = None, header = 0 , sep = ',')

#connecting to the sql server 
mydb = mysql.connector.connect( host = 'localhost', user = 'root', password = 'priyareddy', database = 'storagedata')
mycursor = mydb.cursor() 

#reading the single data file that needs to be pushed into the database 
df = pd.read_csv('single_data.csv', index_col = None, header = 0 , sep = ',', low_memory = False)

#creating a new dataframe dropping the unnecessary columns 
new_df = df.loc[: , ['Id', 'AnlagenbetreiberId','AnlagenbetreiberMaStRNummer', 'Ort', 'Plz', 'AnzahlSolarModule', 'Bruttoleistung', 'Nettonennleistung','EnergietraegerName']]

#filling the Nan values to be zero
new_df = new_df.fillna(0)

#deleting the table storage_data_base if it exists 
mycursor.execute('DROP TABLE storage_data_base')

#Creating a table in the database 
mycursor.execute('''CREATE TABLE 
	                storage_data_base ( Id INT(30), 
	                Plant_Id VARCHAR(255), 
	                MaStRNummer_Id VARCHAR(255), 
	                City VARCHAR(255), 
	                Plz VARCHAR(255), 
	                Number_of_solarmodules VARCHAR(255), 
	                Gross_output VARCHAR(255), 
	                Net_nominal_output VARCHAR(255), 
	                Storage_type VARCHAR(255) )''')    



#Pushing the data from dataframe into the storage_data_base table in the storagedata database
#count = 1
for row in tqdm(new_df.itertuples()):
    sql = 'INSERT INTO storage_data_base (Id,Plant_Id,MaStRNummer_Id, City, Plz, Number_of_solarmodules, Gross_output, Net_nominal_output, Storage_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'  
    val = (row.Id,row.AnlagenbetreiberId,row.AnlagenbetreiberMaStRNummer,row.Ort,row.Plz,row.AnzahlSolarModule,row.Bruttoleistung,row.Nettonennleistung,row.EnergietraegerName) 
    mycursor.execute(sql,val)
    #print( str(count) + ' Data is inserted into the database')
    #count += 1
mydb.commit()
