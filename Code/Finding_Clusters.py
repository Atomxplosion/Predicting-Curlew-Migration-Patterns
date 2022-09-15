import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

startend_df = pd.read_excel('curlewdata_startend.xlsx')
minmax_df = pd.read_excel('curlewdata_minmax.xlsx')

bird_index = [40, 50, 60, 70, 80, 90, 130, 150, 160, 170, 290, 300, 310, 400, 450, 500, 600]
total_lat_diff = 0
total_long_diff = 0
total_time = 0

min_long_arr = []
max_long_arr = []
long_diff = []

min_lat_arr = []
max_lat_arr = []
lat_diff = []

time_arr = []

cluster = []
for i in bird_index: 
    bird_tag = startend_df.iloc[i][1]
    start_long = float(startend_df.iloc[i+1][1])
    start_lat = float(startend_df.iloc[i+2][1])

    #if the start latitude and the start longitude where
    #within specific values, classify as apart of the given cluster
    if(start_long < -115.5) and (start_lat < 44.1): 
        cluster.append(bird_tag)

print(cluster)
  
# cluster 1: ['137441', '126610', '126612', '137439', '137440', '126611', '137438', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524', '199064', '199065', '199063']
# Constraints: if(start_long < -115.5):

# cluster 2: ['128876', '128877', '128879', '148826', '128880', '128878', '170159', '170152', '170150', '170153']
# Constraints: if(-115 <= start_long <= -113) and (start_lat > 45.5):

# cluster 3: ['148830', '148833', '148829', '148825', '148832', '148831', '148834', '160369', '170157', '170158', '170156', '170161', '174744']
# Constraints: if(-113.5 <= start_long <= -109.75)

# Cluster 1 Updated: ['137441', '126610', '126612', '137439', '137440', '126611', '137438', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524']
# Constraints: if(start_long < -115.5) and (start_lat < 44.1):
# [40, 50, 60, 70, 80, 90, 130, 150, 160, 170, 290, 300, 310, 400, 450, 500, 600]

# Cluster 4 ['148828', '148827', '170149', '170148', '170147']
# if(-110 <= start_long <= -108) and (44 < start_lat):

# Cluster 5 ['170151', '170155', '170154', '174740']
# if(-108 <= start_long <= -106):

# Cluster 6 ['174741', '174743', '174742'] 
# if(-105 <= start_long <= -103) and (41 <= start_lat <= 43): 


"""
IGNORE CODE BELOW
"""


#done for the updated Cluster 1
# cluster = []
# bird_index = []
# for i in range(0, 708, 10): 
#     bird_tag = startend_df.iloc[i][1]
#     start_long = float(startend_df.iloc[i+1][1])
#     start_lat = float(startend_df.iloc[i+2][1])
#     if(start_long < -115.5) and (start_lat < 44.1):
#         cluster.append(bird_tag)
#         bird_index.append(i)
# print(bird_tag_index)



# for i in range(len(bird_index)):
#     min_long_data = minmax_df.iloc[bird_index[i] + 1]
#     min_long = float(min_long_data[0])
#     min_long_arr.append(min_long)

#     max_long_data = minmax_df.iloc[bird_index[i] + 2]
#     max_long = float(max_long_data[0])
#     max_long_arr.append(max_long)

#     long_diff.append(abs(min_long - max_long))

#     min_lat_data = minmax_df.iloc[bird_index[i] + 4]
#     min_lat = float(min_lat_data[0])
#     min_lat_arr.append(min_lat)
 
#     max_lat_data = minmax_df.iloc[bird_index[i] + 5]
#     max_lat = float(max_lat_data[0])
#     max_lat_arr.append(max_lat)

#     lat_diff.append(abs(min_lat - max_lat))

#     time = minmax_df.iloc[bird_index[i]+7][0]
#     time_arr.append(time)

# print(len(min_long_arr))
# print(len(max_long_arr))
# print(len(long_diff))
# print(" ")
# print(" ")

# print(len(min_lat_arr))
# print(len(max_lat_arr))
# print(len(lat_diff))
# print(" ")
# print(" ")

# print(len(time_arr))

# print(min_long_arr)
# print(max_long_arr)
# print(long_diff)
# print(" ")
# print(" ")

# print(min_lat_arr)
# print(max_lat_arr)
# print(lat_diff)
# print(" ")
# print(" ")

# print(time_arr)


# long_increment = (total_long_diff/(len(bird_index)*50))
# lat_increment = (total_lat_diff/(len(bird_index)*50))
# time_increment = (total_time/(len(bird_index)*50))

# print(long_increment)
# print(lat_increment)
# print(time_increment)

# longitude increment 0.14827400000000004
# latitude increment 0.2388925294117647
# time increment 47395.29882352941

  # end_long = float(startend_df.iloc[i+5][1])  
    # end_lat = float(startend_df.iloc[i+6][1])
    # end_time = float(startend_df.iloc[i+7][1])