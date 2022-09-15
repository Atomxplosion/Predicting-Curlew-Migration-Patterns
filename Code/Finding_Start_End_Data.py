import pandas as pd
import xlsxwriter

migrationpath = []
bird_tag = []

#state which csv or excel you are using
migration_df = pd.read_csv('curlewmigration.csv')

#261671 FILLED DATAPOINTS (loop for 1 to (261671 - 1))
#google colab can only handle around 25,000 datapoints, just ran this own my own computer (siddh)
#loop for 1 to row 82662 (82662 is the last row for this specific animal tag)
#60 columns, 71 unique tags

# .iloc to get that specifc cell or get the row
# [row] [column]

datapoint = migration_df.iloc[0]
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
print(original_date)

migrationpath.append([[lon, lat, 0]])
bird_tag.append(tag)

#go through all datapoint
for i in range(1, 261670):
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

#if the bird tag of the datapoint is not already seen create a new bird path array
  if (tag != bird_tag[len(bird_tag)-1]):
    original_date = [date, time]
    migrationpath.append([[lon, lat, 0]])
    bird_tag.append(tag)
  else:
    #convert the timestamp into value of minutes
    #T in minutes is based on the original date that the bird started traveling
    #ex: First Date: 1/1/2022 1:00 PM -> Second Date: 1/1/2022 1:10 PM, T = 10
    t = 0
    t += 12*30*24*60*(int(date[0]) - int(original_date[0][0]))
    t += 30*24*60*(int(date[1]) - int(original_date[0][1]))
    t += 24*60*(int(date[2]) - int(original_date[0][2]))

    t += 10*60*(int(time[0][0]) - int(original_date[1][0][0]))
    t += 60*(int(time[0][1]) - int(original_date[1][0][1]))
    t += 10*(int(time[1][0]) - int(original_date[1][1][0]))
    t += (int(time[1][1]) - int(original_date[1][1][1]))
    migrationpath[len(bird_tag)-1].append([lon, lat, t])

data = []
des = []

#print out the first datapoint and the last datapoint for each bird's migration path
for i in range(len(migrationpath)):
  data.append(str(bird_tag[i]))
  data.append(str(migrationpath[i][0][0]))
  data.append(str(migrationpath[i][0][1]))
  data.append(str(migrationpath[i][0][2]))
  data.append("  ")
  data.append(str(migrationpath[i][len(migrationpath[i])-1][0]))
  data.append(str(migrationpath[i][len(migrationpath[i])-1][1]))
  data.append(str(migrationpath[i][len(migrationpath[i])-1][2]))
  data.append("  ")
  data.append("  ")
  

  des.append("bird tag")
  des.append("start longitude")  
  des.append("start latitude")
  des.append("start time")
  des.append("  ")
  des.append("ending longitude")  
  des.append("ending latitude")   
  des.append("ending time")   
  des.append("  ")
  des.append("  ")
   
df = pd.DataFrame(data, des)
writer = pd.ExcelWriter('curlewdata_startend.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
print("finished")