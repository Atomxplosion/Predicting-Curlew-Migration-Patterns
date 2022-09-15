import pandas as pd
import xlsxwriter

migrationpath = []
bird_tag = []

migration_df = pd.read_csv('curlewmigration.csv')

#261671 FILLED DATAPOINTS (loop for 1 to (261671 - 1))
#google colab can only handle around 25,000 datapoints, just ran this own my own computer (siddh)
#loop for 1 to row 82662 (82662 is the last row for this specific animal tag)
#60 columns, 71 unique tags


#SAME INITIAL CODE AS Finding_T_Data 
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

  if (tag != bird_tag[len(bird_tag)-1]):
    original_date = [date, time]
    migrationpath.append([[lon, lat, 0]])
    bird_tag.append(tag)
  else:
    t = 0
    t += 12*30*24*60*(int(date[0]) - int(original_date[0][0]))
    t += 30*24*60*(int(date[1]) - int(original_date[0][1]))
    t += 24*60*(int(date[2]) - int(original_date[0][2]))

    t += 10*60*(int(time[0][0]) - int(original_date[1][0][0]))
    t += 60*(int(time[0][1]) - int(original_date[1][0][1]))
    t += 10*(int(time[1][0]) - int(original_date[1][1][0]))
    t += (int(time[1][1]) - int(original_date[1][1][1]))
    migrationpath[len(bird_tag)-1].append([lon, lat, t])


#print out min and max of each array to get range of data

data = []
des = []
for i in range(len(migrationpath)):
  lon = []
  lat = []
  t = []
  for j in range(len(migrationpath[i])):
    lon.append(migrationpath[i][j][0])
    lat.append(migrationpath[i][j][1])
    t.append(migrationpath[i][j][2])
  data.append(bird_tag[i])
  des.append("bird tag")

  data.append(min(lon))
  des.append("min longitude")

  data.append(max(lon))
  des.append("max longitude")

  data.append("   ")
  des.append("   ")

  data.append(min(lat))
  des.append("min latitude")

  data.append(max(lat))
  des.append("max latitude")

  data.append("   ")
  des.append("   ")

  data.append(max(t))
  des.append("maximum time")

  data.append("   ")
  des.append("   ")
  data.append("   ")
  des.append("   ")

df = pd.DataFrame(data, des)
writer = pd.ExcelWriter('curlewdata_minmax.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
print("finished")