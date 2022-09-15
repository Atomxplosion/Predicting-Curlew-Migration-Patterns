import pandas as pd
import numpy as np
import xlsxwriter
import math

migrationpath = []
bird_tag = []

migration_df = pd.read_csv('curlewmigration.csv')

#261671 FILLED DATAPOINTS (loop for 1 to (261671 - 1))
#google colab can only handle around 25,000 datapoints, just ran this own my own computer (siddh)
#loop for 1 to row 82662 (82662 is the last row for this specific animal tag)
#60 columns, 71 unique tags


#IGNORE THE COMMENTED OUT ARRAYS
# '126612', '137439', '137440', '126611', '137438', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524'
#'137438'
# bird_tags = ['137441', '126610', '126612', '137439', '137440', '126611', '137438', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524']

cluster_tag = ['137441', '126610', '126612', '137439', '137440', '126611', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524']

# min_long = [-116.278, -120.4, -123.136, -116.3, -116.284, -121.22828, -121.35276, -121.18816, -121.11373, -121.48889, -120.36274, -121.55254, -122.82357, -117.14452, -119.94979, -116.41286, -120.10905]
# max_long = [-109.56033, -114.92974, -116.219, -111.96912, -100.74203, -116.253, -114.35011, -115.73225, -104.95647, -116.46307, -109.8023, -113.55557, -112.2404, -112.96681, -111.19528, -114.35856, -115.79795]

# min_lat = [26.95485, 32.6712, 35.92972, 31.065, 22.67196, 35.125, 32.60069, 37.0638, 31.41644, 36.85688, 27.07145, 32.4148, 32.90806, 31.72885, 31.63507, 32.82689, 35.69924]
# max_lat = [44.65615, 43.94544, 43.963, 44.54623, 43.783, 43.907, 44.15545, 44.53252, 44.44161, 43.88946, 44.64536, 43.52338, 44.46138, 43.50631, 44.67692, 43.45663, 43.60871]

# total_time = [2570594, 3232821, 1636700, 1901324, 2119642, 2040595, 4316499, 2216987, 3797378, 273406, 3260071, 3277934, 3274658, 2766285, 1432087, 434207, 1734816]

min_long = [-116.278, -120.4, -123.136, -116.3, -116.284, -121.22828, -121.18816, -121.11373, -121.48889, -120.36274, -121.55254, -122.82357, -117.14452, -119.94979, -116.41286, -120.10905]
max_long = [-109.56033, -114.92974, -116.219, -111.96912, -100.74203, -116.253, -115.73225, -104.95647, -116.46307, -109.8023, -113.55557, -112.2404, -112.96681, -111.19528, -114.35856, -115.79795]

min_lat = [26.95485, 32.6712, 35.92972, 31.065, 22.67196, 35.125, 37.0638, 31.41644, 36.85688, 27.07145, 32.4148, 32.90806, 31.72885, 31.63507, 32.82689, 35.69924]
max_lat = [44.65615, 43.94544, 43.963, 44.54623, 43.783, 43.907, 44.53252, 44.44161, 43.88946, 44.64536, 43.52338, 44.46138, 43.50631, 44.67692, 43.45663, 43.60871]

# total_time = [2570594, 3232821, 1636700, 1901324, 2119642, 2040595, 2216987, 3797378, 273406, 3260071, 3277934, 3274658, 2766285, 1432087, 434207, 1734816]
total_time = [158.35386904761904, 270.5125992063492, 162.2045634920635, 187.91815476190476, 210.26329365079366, 149.12787698412697, 219.93125, 186.4375992063492, 26.932936507936507, 167.18968253968254, 221.9734126984127, 221.5076388888889, 274.23581349206347, 36.43611111111111, 42.487003968253966, 171.5013888888889]

# og_length = [191, 254, 155, 176, 190, 163, 312, 208, 219, 27, 245, 258, 258, 250, 52, 38, 158]
og_length = [191, 254, 155, 176, 190, 163, 208, 219, 27, 245, 258, 258, 250, 52, 38, 158]

time_arr = []
lon_arr = []
lat_arr = []

x_vector_arr = []
y_vector_arr = []
t_vector_arr = []

x_weight_arr = []
y_weight_arr = []
t_weight_arr = []

x_increment_arr = []
y_increment_arr = []
t_increment_arr = []

#increment values
long_inc = 0.5
lat_inc = 1
time_inc = 10

#first datapoint from bird in cluster
datapoint = migration_df.iloc[27679]
time = datapoint[2]
lon = datapoint[3]
lat = datapoint[4]
tag = datapoint[57]
time = time.split(" ")
date = time[0]
time = time[1]
date = date.split("-")
time = time.split(":")
original_date = [date, time]
j = 0

lon_arr.append(lon)
lat_arr.append(lat)
time_arr.append(0)
bird_tag.append(tag)

t = 0

print("hello")

#start on row 27681 - 1
for i in range(27680, 261670):
  datapoint = migration_df.iloc[i]
  time = datapoint[2]
  lon = datapoint[3]
  lat = datapoint[4]
  tag = datapoint[57]
  time = time.split(" ")
  date = time[0]
  time = time[1]
  date = date.split("-")
  time = time.split(":")

  prev_datapoint = migration_df.iloc[i-1]
  prev_tag = prev_datapoint[57]

  #if the tag changes from datapoint to datapoint, that means that
  #a new bird's migration path data is being stated
  if (tag != prev_tag):
    #if the previous tag was a tag within our cluster, save the bird data
    if (str(prev_tag) == cluster_tag[j]):
      print(j)
      print(len(lon_arr))
      total_time.append(time_arr[len(time_arr)-1])
      migrationpath = [lon_arr, lat_arr, time_arr, x_vector_arr, y_vector_arr, t_vector_arr, x_weight_arr, x_increment_arr, y_weight_arr, y_increment_arr, t_weight_arr, t_increment_arr]
      df = pd.DataFrame(migrationpath)
      writer = pd.ExcelWriter(str(cluster_tag[j] + 'migration.xlsx'), engine='xlsxwriter')
      df.to_excel(writer, sheet_name='Sheet1')
      writer.save()

      #reset all of the values
      t = 0

      migrationpath = []

      lon_arr = []
      lat_arr = []
      time_arr = []

      x_vector_arr = []
      y_vector_arr = []
      t_vector_arr = []

      x_weight_arr = []
      x_increment_arr = []

      y_weight_arr = []
      y_increment_arr = []

      t_weight_arr = []
      t_increment_arr = []
  
  #just to check that the computer doesn't accidentally increment after the last tag
    if (j < 15):
      #if the first datapoint of the bird is apart of the cluster
      #then reset OG Date and time
      if (tag == int(cluster_tag[j+1])): 
        j += 1
        original_date = [date, time]
        lon_arr.append(lon) 
        lat_arr.append(lat)
        time_arr.append(0)

        bird_tag.append(tag)

  elif (tag == int(cluster_tag[j])):
    #convert Time into Minutes
    t = 0
    t += 12*30*24*60*(int(date[0]) - int(original_date[0][0]))
    t += 30*24*60*(int(date[1]) - int(original_date[0][1]))
    t += 24*60*(int(date[2]) - int(original_date[0][2]))

    t += 10*60*(int(time[0][0]) - int(original_date[1][0][0]))
    t += 60*(int(time[0][1]) - int(original_date[1][0][1]))
    t += 10*(int(time[1][0]) - int(original_date[1][1][0]))
    t += (int(time[1][1]) - int(original_date[1][1][1]))


  #if the cumulative minutes go over the num of minutes in a week, save the data
  #do this to work with weeks instead of minutes, generalizes data more
    if ( ((t/10080)-time_arr[len(time_arr)-1]) >= 1):

      #check to make sure to remove any data before or after a major timeskip
      if (((t/10080)-time_arr[len(time_arr)-1]) >= 25):
        #if there is very little data before the timeskip, remove that data
        #and start from the timeskip point
        if (((og_length[j] - len(time_arr)) >= len(time_arr))):
          og_length[j] = og_length[j] - len(time_arr)
          lon_arr.clear()
          lat_arr.clear()
          time_arr.clear()

          original_date = [date, time]
          lon_arr.append(lon)
          lat_arr.append(lat)
          time_arr.append(0)

          x_weight_arr.clear()
          x_vector_arr.clear()
          x_increment_arr.clear()

          y_weight_arr.clear()
          y_vector_arr.clear()
          y_increment_arr.clear()

          t_weight_arr.clear()
          t_vector_arr.clear()
          t_increment_arr.clear()
        #don't add the data if it is after a major timeskip and there isn't alot of data
        else:
          continue

      #if there is no major timeskip, simply add the data to the array
      else:
        lon_arr.append(lon)
        lat_arr.append(lat)
        time_arr.append(t/10080)
      
      #if there is more than one datapoint, then you can calculate the vector
        if (len(lon_arr) > 1):
          #calculate change in time
          change_time = time_arr[len(time_arr)-1] -time_arr[len(time_arr)-2]

          # x_vector_arr.append((lon_arr[len(lon_arr)-1] - lon_arr[len(lon_arr)-2]))
          # y_vector_arr.append((lat_arr[len(lat_arr)-1] - lat_arr[len(lat_arr)-2]))

          #calculate x vector (longitude)
          x_vector_arr.append((lon_arr[len(lon_arr)-1] - lon_arr[len(lon_arr)-2])/change_time)
          #calculate y vector (latitude)
          y_vector_arr.append((lat_arr[len(lat_arr)-1] - lat_arr[len(lat_arr)-2])/change_time)
          #calculate t vector (time)
          t_vector_arr.append(change_time)
          

          #repeated for lat and time
          for k in np.arange(math.floor(min_long[j]), math.ceil(max_long[j]+long_inc), long_inc):
            #find increment range that the data falls into
            if (k <= lon_arr[len(lon_arr)-2] <= k+long_inc):
              #calculate weight based on increment values
              x_weight = (lon_arr[len(lon_arr)-2]-k)/long_inc
              x_weight_arr.append(x_weight)
              x_increment_arr.append(k)
              break

          for k in np.arange(math.floor(min_lat[j]), math.ceil(max_lat[j]+lat_inc), lat_inc):
            if (k <= lat_arr[len(lat_arr)-2] <= k+lat_inc):
              y_weight = (lat_arr[len(lat_arr)-2]-k)/lat_inc
              y_weight_arr.append(y_weight)
              y_increment_arr.append(k)
              break

          for k in np.arange(0, math.ceil(total_time[j]+time_inc), time_inc):
            if (k <= time_arr[len(time_arr)-2] <= k+time_inc):
              #use e^(-alpha x |change in time|/time inc)
              #alpha = 1/2 in our case, alpha is purely experimental
              t_weight = math.exp(-2.5*((abs(time_arr[len(time_arr)-2] - k))/time_inc)/5)
              t_weight_arr.append(t_weight)
              t_increment_arr.append(k)
              break

print(total_time)
print("totally done")