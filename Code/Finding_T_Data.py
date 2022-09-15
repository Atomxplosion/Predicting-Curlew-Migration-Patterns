import pandas as pd
import xlsxwriter

migrationpath = []
bird_tag = []

migration_df = pd.read_csv('curlewmigration.csv')

#261671 FILLED DATAPOINTS (loop for 1 to (261671 - 1))
#google colab can only handle around 25,000 datapoints, just ran this own my own computer (siddh)
#loop for 1 to row 82662 (82662 is the last row for this specific animal tag)
#60 columns, 71 unique tags

datapoint = migration_df.iloc[0]
time = datapoint[2]
lon = datapoint[3]
lat = datapoint[4]
tag = datapoint[57]

#split the timestamp into multiple numbers to conver it to T
time = time.split(" ")
date = time[0]
time = time[1]
date = date.split("-")
time = time.split(":")
original_date = [date, time]

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
    #convert year to minutes
    t += 12*30*24*60*(int(date[0]) - int(original_date[0][0]))
    #convert month to minutes
    t += 30*24*60*(int(date[1]) - int(original_date[0][1]))
    #convert days to minutes
    t += 24*60*(int(date[2]) - int(original_date[0][2]))

    #convert tens place of the hour to minutes
    t += 10*60*(int(time[0][0]) - int(original_date[1][0][0]))
    #convert ones place of the hour to minutes
    t += 60*(int(time[0][1]) - int(original_date[1][0][1]))
    #convert tens place of the minutes to minutes
    t += 10*(int(time[1][0]) - int(original_date[1][1][0]))
    #add minutes to T
    t += (int(time[1][1]) - int(original_date[1][1][1]))
    #add the coordinate to the bird's path
    migrationpath[len(bird_tag)-1].append([lon, lat, t])

data = []
#print out migration path values
for i in range(len(migrationpath)):
  data.append(str(bird_tag[i]))
  data.append("      ")
  data.append(str(migrationpath[i]))
  data.append("      ")
  data.append(str(migrationpath[i][0]))
  data.append("      ")
  data.append(str(migrationpath[i][len(migrationpath[i])-1]))
  data.append("      ")
  data.append("      ")
  data.append("      ")
  
data.append(migrationpath)

#save values to an Excel Spreadsheet
df = pd.DataFrame(data)
writer = pd.ExcelWriter('curlewdata_time.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
print("finished")