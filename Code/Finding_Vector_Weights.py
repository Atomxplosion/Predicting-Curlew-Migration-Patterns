import pandas as pd
import math
import numpy as np

#weight_opp = 1 - weight
x_weight = []
x_weightopp = []
x_weight_increment = []

bird_tags = ['137441', '126610', '126612', '137439', '137440', '126611', '137438', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524']

min_long = [-116.278, -120.4, -123.136, -116.3, -116.284, -121.22828, -121.35276, -121.18816, -121.11373, -121.48889, -120.36274, -121.55254, -122.82357, -117.14452, -119.94979, -116.41286, -120.10905]
max_long = [-109.56033, -114.92974, -116.219, -111.96912, -100.74203, -116.253, -114.35011, -115.73225, -104.95647, -116.46307, -109.8023, -113.55557, -112.2404, -112.96681, -111.19528, -114.35856, -115.79795]

min_lat = [26.95485, 32.6712, 35.92972, 31.065, 22.67196, 35.125, 32.60069, 37.0638, 31.41644, 36.85688, 27.07145, 32.4148, 32.90806, 31.72885, 31.63507, 32.82689, 35.69924]
max_lat = [44.65615, 43.94544, 43.963, 44.54623, 43.783, 43.907, 44.15545, 44.53252, 44.44161, 43.88946, 44.64536, 43.52338, 44.46138, 43.50631, 44.67692, 43.45663, 43.60871]

time = [2570594, 3232821, 1636700, 1901324, 2119642, 2040595, 4316499, 2216987, 3797378, 273406, 3260071, 3277934, 3274658, 2766285, 1432087, 434207, 1734816]

x_weight_arr = []
x_increment_arr = []

y_weight_arr = []
y_increment_arr = []

# longitude increment 0.14827400000000004
#long increment = 0.15
# latitude increment 0.2388925294117647
#lat increment = 0.25
# time increment 47395.29882352941
#time increment = 50000

#our increments lat and long are degrees, time is in minutes
long_inc = 0.15
lat_inc = 0.25
time_inc = 50000

#repeat for y (lat)
#done for x (long)
for i in range(len(bird_tags)):
    #access bird's spreadsheet containing its migration values
    bird_path_df = pd.read_excel(str(bird_tags[i] + 'migration.xlsx'))
    long_arr = bird_path_df.iloc[1]
    #go through all the values in the migration dataset
    for j in range(1, len(long_arr)):
        #check in what increment range does the datapoint fit into 
        for k in np.arange(math.floor(min_long[i]), math.ceil(max_long[i]+long_inc), long_inc):
            #if the value is in between increment 1 and increment 2, save value
            if (float(k) <= float(long_arr[j]) <= float(k+long_inc)):
                #calcluate the weight
                x_weight = (float(k) - float(long_arr[j]))/long_inc
                x_weight_arr.append(x_weight)
                x_increment_arr.append(k)

    #save data to spreadsheet
    x_values = [x_weight_arr, x_increment_arr]
    df = pd.DataFrame(x_values)
    writer = pd.ExcelWriter(str(bird_tags[i] + 'migration.xlsx'), engine='xlsxwriter')
    df.to_excel(writer, sheet_name = 'Sheet1', startrow = 7, index = False, Header = False)
    writer.save()

    x_weight_arr = []
    x_increment_arr = []
    print(i)
print("totally finished")
             

# for i in range(len(bird_tags)):
#     bird_path_df = pd.read_excel(str(bird_tags[i] + 'migration.xlsx'))
#     long_arr = bird_path_df.iloc[1]
#     for j in range(len(long_arr)):
#         for k in range(min_long[i], max_long[i], long_inc):
#             if (k <= long_arr[j] <= k+long_inc):
#                 x_weight = (k - long_arr[j])/long_inc
#                 x_weight_arr.append(x_weight)
#                 x_increment_arr.append(k)
#             if((max_long[i] - k) < long_inc):  
#                 k = max_long[i]   