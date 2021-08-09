# integrated-project
Geographical mapping of storage systems to substations

##Motivation 
There is a tremendous shift to renewable power generation which leads to a lot of storage systems connected to the grid , since all the storage systems reach its peak production mostly at the same time feeding the energy back to the grid may cause grid instability. Hence the primary task was to see the storage systems affect which substation, directly or indirectly, that can help to troubleshoot which storage system is causing the imbalance. The end result has to be formulated in a matrix. Matrix will be useful for performing the load flow studies and helps the operator analyze which interconnector has most storage connections and the contingency planning can be made accordingly.

##Steps
Geocoded zipcode file consists of the geographical corrdinates of Germany zipcodes

Storage data file pushes the large storage data file onto a sql database

adding-zipcode-properties will add the storage system data to the geocoded zipcode
%% the assumption here is that the storage data under the same zipcode are clubbed together

mapping-closest substation will map the storage systems data to closest substation by calculating the distance
between zipcode and every substation.

matrix formulation will formulate the matrices based on the connections made in the previous step
These atrices are used for load flow studies

zipcode-interconnector-connections will decide the storage systems that have an effect on the transmission
line interconnector 

