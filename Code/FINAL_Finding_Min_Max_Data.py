import pandas as pd
import numpy as np

min_long = []
max_long = []

min_lat = []
max_lat = []

max_time = []

long_arr = []
lat_arr = []

bird_tags = ['137441', '126610', '126612', '137439', '137440', '126611', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524']

#go through each bird's migration values
for i in range(len(bird_tags)):
    migration_values_df = pd.read_excel(str(bird_tags[i] + 'migration.xlsx'))
    long = migration_values_df.iloc[0]
    lat = migration_values_df.iloc[1]
    time = migration_values_df.iloc[2]
    #go through the entire dataset
    #check in case a datapoint is accidently recorded as 0
    for j in range(len(long)-1):
        if (long[j] != 0):
            long_arr.append(long[j])
        if (lat[j] != 0):
            lat_arr.append(lat[j])

    #append min and max values to array
    max_long.append(max(long_arr))
    min_long.append(min(long_arr))
    max_lat.append(max(lat_arr))
    min_lat.append(min(lat_arr))
    max_time.append(max(time))
    
#     max_time.append(max(time))

#print out max and min of each bird
print(max_long)
print(min_long)
print(max_lat)
print(min_lat)
print(max_time)
    