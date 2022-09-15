import csv
import scipy as sci

lat_cords = []
long_cords = []
file = open('adlie_penguins.csv')
penguin_migration = csv.reader(file)
print(penguin_migration)
penguin = True
i = 1

for i in range(10):
    long_cords.append(penguin_migration[3][i+1])
    lat_cords.append(penguin_migration[4][i+1])
print(long_cords)
print(lat_cords)