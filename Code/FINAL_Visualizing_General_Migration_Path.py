import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

startend_df = pd.read_excel('curlewdata_startend.xlsx')
timestamp_df = pd.read_excel('curlewdata_timestamp.xlsx')

fig, ax = plt.subplots(figsize = (25, 25))

#Go through start end and timestamp datasheet
for i in range(0, 708, 10): 
    bird_tag = startend_df.iloc[i][1]
    start_long = float(startend_df.iloc[i+1][1])
    start_lat = float(startend_df.iloc[i+2][1])

    end_long = float(startend_df.iloc[i+5][1])  
    end_lat = float(startend_df.iloc[i+6][1])
    end_time = float(startend_df.iloc[i+7][1])

    # dist_long = (start_long + 104)**2 + (end_long + 103)**2
    # dist_lat = (start_lat - 46)**2 + (end_lat - 34)**2
    # distance = (dist_lat + dist_long)**0.5 
    timestamp_row = timestamp_df.iloc[i+6]
    timestamp = timestamp_row[0]
    # print(time_stamp)

    #convert string year into int
    year = int(timestamp[len(timestamp)-25:len(timestamp)-21])

    #based on year color the vectors a different color
    #plot vector from start lat and long to ending lat and long
    #describes general path of the bird, i.e. its starting and ending
    ax.quiver(start_long, start_lat, end_long, end_lat, color = str("C" + str(year-2013)))

plt.show()


"""
IGNORE BELOW CODE
"""


#     if (distance < 10):
#         first_cluster.append(bird_tag)
#     else:
#         second_cluster.append(bird_tag)
    

# df = pd.DataFrame(first_cluster, second_cluster)
# writer = pd.ExcelWriter('curlewdata_startend.xlsx', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='Sheet1')
# writer.save()
# print("finished")

# print(first_cluster)
# print(second_cluster)



# cluster1 = []
# cluster2 = []
# for i in range(10, 708, 10): 
#     bird_tag = startend_df.iloc[i][1]
#     start_long = startend_df.iloc[i+1][1]   
#     start_lat = startend_df.iloc[i+2][1]

#     end_long = startend_df.iloc[i+5][1]   
#     end_lat = startend_df.ilimport matplotlib.pyplot as pltoc[i+6][1]
#     end_time = startend_df.iloc[i+7][1]

#     if (-104 <= float(start_long) <= -100) and (-104 <= float(end_long) <= -100):
#         if (44 <= float(start_lat) <= 48) and (32 <= float(end_lat) <= 36):
#             cluster1.append(bird_tag)
#         else:
#             cluster2.append(bird_tag)
#     else:
#         cluster2.append(bird_tag)

# print("cluster 1")
# print(cluster1)
# print(" cluster 2")
# print(cluster2)
# print("finished")