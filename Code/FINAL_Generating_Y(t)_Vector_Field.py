import pandas as pd
import numpy as np
from statistics import mean
import xlsxwriter
import math


bird_tags = ['137441', '126610', '126612', '137439', '137440', '126611', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524']

min_long = [-116.278, -120.4, -123.136, -116.3, -116.284, -121.22828, -121.18816, -121.11373, -121.48889, -120.36274, -121.55254, -122.82357, -117.14452, -119.94979, -116.41286, -120.10905]
max_long = [-109.56033, -114.92974, -116.219, -111.96912, -100.74203, -116.253, -115.73225, -104.95647, -116.46307, -109.8023, -113.55557, -112.2404, -112.96681, -111.19528, -114.35856, -115.79795]

min_lat = [26.95485, 32.6712, 35.92972, 31.065, 22.67196, 35.125, 37.0638, 31.41644, 36.85688, 27.07145, 32.4148, 32.90806, 31.72885, 31.63507, 32.82689, 35.69924]
max_lat = [44.65615, 43.94544, 43.963, 44.54623, 43.783, 43.907, 44.53252, 44.44161, 43.88946, 44.64536, 43.52338, 44.46138, 43.50631, 44.67692, 43.45663, 43.60871]

total_time = [158.35386904761904, 270.5125992063492, 162.2045634920635, 187.91815476190476, 210.26329365079366, 149.12787698412697, 219.93125, 186.4375992063492, 26.932936507936507, 167.18968253968254, 221.9734126984127, 221.5076388888889, 274.23581349206347, 36.43611111111111, 42.487003968253966, 171.5013888888889]

long_inc = 0.5
lat_inc = 1
time_inc = 10

print("hi")

"""
EXACT SAME CODE AS X VECTOR FIELDS BUT FOR LATITUDE
CHECK COMMENTS OF X(t) VECTOR FIELD TO UNDERSTAND CODE 
"""

for i in range(len(bird_tags)):
    x_vector_field = []
    y_vector_field = []

    x_increment = []
    y_increment = []
    t_increment = []
    
    for j in np.arange((math.ceil(max_lat[i]+lat_inc) - math.floor(min_lat[i]))/ lat_inc):
        x_increment.append(j*lat_inc+math.floor(min_lat[i]))
        x_vector_field.append([])
        
    for j in range(len(x_vector_field)):
        for k in np.arange(0, math.ceil(total_time[i]+time_inc), time_inc):
            x_vector_field[j].append([])

    for j in range(0, math.ceil(total_time[i]+time_inc), time_inc):
        t_increment.append(j)

    migration_values_df = pd.read_excel(str(bird_tags[i] + 'migration.xlsx'))

    lat_vector = migration_values_df.iloc[4]

    lat_weight = migration_values_df.iloc[8]
    lat_value = migration_values_df.iloc[1]

    time_value = migration_values_df.iloc[2]
    time_increment = migration_values_df.iloc[11]

    change_time = migration_values_df.iloc[2]

    for j in range(len(lat_vector)-3):
        # x_index = BinarySearch(x_increment, lat_increment[j])
        for k in range(len(x_increment)-1):
            if (x_increment[k] <= lat_value[j] <= x_increment[k+1]):
                x_index = k
            if (x_increment[k] <= lat_value[j+1] <= x_increment[k+1]):
                next_x_index = k

        for k in range(len(t_increment)):
            #/10000 if minutes
            time_weight = math.exp(-2.5* abs(t_increment[k]-time_value[j]))
            x_value_1 = lat_vector[j] * lat_weight[j]*time_weight
            #this part may be the reason for the erorr, logical error
            for l in range(next_x_index - x_index + 1):
                if (np.isnan(x_value_1) == False) and (np.isinf(x_value_1) == False):
                    x_vector_field[x_index+l][k].append(x_value_1)
                else:
                    x_vector_field[x_index+l][k].append(0)
                x_value_2 = lat_vector[j] * (1-lat_weight[j])*time_weight
                if (np.isnan(x_value_2) == False) and (np.isinf(x_value_2) == False):
                    x_vector_field[x_index+1+l][k].append(x_value_2)
                else:
                    x_vector_field[x_index+1+l][k].append(0)
            # if (np.isnan(x_value_1) == False) and (np.isinf(x_value_1) == False):
            #     x_vector_field[x_index][k].append(x_value_1)
            # else:
            #     x_vector_field[x_index][k].append(0)
            # x_value_2 = lat_vector[j] * (1-lat_weight[j])*time_weight
            # if (np.isnan(x_value_2) == False) and (np.isinf(x_value_2) == False):
            #     x_vector_field[x_index+1][k].append(x_value_2)
            # else:
            #     x_vector_field[x_index+1][k].append(0)
            
            
    for j in range(len(x_vector_field)):
        for k in range(len(x_vector_field[0])):
            if (len(x_vector_field[j][k]) >0):
                x_vector_field[j][k] = sum(x_vector_field[j][k])   
            else:
                x_vector_field[j][k] = 0   
    df = pd.DataFrame(np.array(x_vector_field))
    writer = pd.ExcelWriter(str(bird_tags[i] + 'yvectorfield.xlsx'), engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print(i)

print("totally finished")