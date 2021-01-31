import pandas as pd
import geopy as gp
from geopy.distance import geodesic 
from tqdm.auto import tqdm

substation_df = pd.read_csv('distributed-substation.csv', header = 0 , index_col = None)
print(substation_df)

zipcode_df = pd.read_csv('filtered_storageSystems.csv', header = 0 ,index_col = None, sep = ',')
print(zipcode_df)


zipcode_df['closest substation lat'] = 0
zipcode_df['closest substation lon'] = 0
zipcode_df['UW'] = 0
zipcode_df['50HZ'] = 0
zipcode_df['VNB'] = 0


for i in tqdm(zipcode_df.index):
    lst = []
    point1 = (zipcode_df.loc[i,'lat'],zipcode_df.loc[i,'lon'])
    for j in substation_df.index:
        point2 = (substation_df.loc[j,'lat'],substation_df.loc[j,'long'])
        distance = geodesic(point1,point2).miles
        lst.append(distance)
    #print( " The list that contains the distance between the first zipcode and every substation is " + str(lst))
    closest_substation = lst.index(min(lst))
    zipcode_df.loc[i,'closest substation lat'] = substation_df.loc[closest_substation, 'lat']
    zipcode_df.loc[i, 'closest substation lon'] = substation_df.loc[closest_substation,'long']
    zipcode_df.loc[i, 'UW'] = substation_df.loc[closest_substation, 'UW']
    zipcode_df.loc[i, '50HZ'] = substation_df.loc[closest_substation, '50HZ']
    zipcode_df.loc[i, 'VNB'] = substation_df.loc[closest_substation, 'VNB']


zipcode_df.to_csv('final_data.csv', index = False)
zipcode_df.to_excel('final_data.xlsx', sheet_name = 'final_data')    
