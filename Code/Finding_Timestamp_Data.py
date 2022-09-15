import pandas as pd
import xlsxwriter

#total migration path for all the birds (3D Array)
# All Birds Migration Path (1D) -> Specific Bird's Migration Path (2D) 
# -> Bird's Coordinates Saved in 3 value Array (lon, lat, time) (3D)  
migrationpath = []

#saves all bird tags
bird_tag = []

#get file containing migration data
migration_df = pd.read_csv('curlewmigration.csv')

#261671 FILLED DATAPOINTS (loop for 1 to (261671 - 1))
#google colab can only handle around 25,000 datapoints, just ran this own my own computer (siddh)
#loop for 1 to row 82662 (82662 is the last row for this specific animal tag)
#60 columns, 71 unique tags

#Get datapoint at row 0
datapoint = migration_df.iloc[0]

#get value at column the given index
time = datapoint[2]
lon = datapoint[3]
lat = datapoint[4]
tag = datapoint[57]

migrationpath.append([[lon, lat, time]])
bird_tag.append(tag)

#go through all datapoint
for i in range(1, 261670):
  datapoint = migration_df.iloc[i]
  time = str(datapoint[2])
  lon = int(datapoint[3])
  lat = int(datapoint[4])
  tag = int(datapoint[57])
  #if the bird tag of the datapoint is not already seen create a new bird path array
  if (tag != bird_tag[len(bird_tag)-1]):
    migrationpath.append([[lon, lat, time]])
    bird_tag.append(tag)
  else:
    migrationpath[len(bird_tag)-1].append([lon, lat, time])

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
  
#save values to an Excel Spreadsheet
df = pd.DataFrame(data)
writer = pd.ExcelWriter('curlewdata_timestamp.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
print("finished")