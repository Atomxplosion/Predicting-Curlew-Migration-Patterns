import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

min_long = [-116.278, -120.4, -123.136, -116.3, -116.284, -121.22828, -121.18816, -121.11373, -121.48889, -120.36274, -121.55254, -122.82357, -117.14452, -119.94979, -116.41286, -120.10905]
max_long = [-109.56033, -114.92974, -116.219, -111.96912, -100.74203, -116.253, -115.73225, -104.95647, -116.46307, -109.8023, -113.55557, -112.2404, -112.96681, -111.19528, -114.35856, -115.79795]

min_lat = [26.95485, 32.6712, 35.92972, 31.065, 22.67196, 35.125, 37.0638, 31.41644, 36.85688, 27.07145, 32.4148, 32.90806, 31.72885, 31.63507, 32.82689, 35.69924]
max_lat = [44.65615, 43.94544, 43.963, 44.54623, 43.783, 43.907, 44.53252, 44.44161, 43.88946, 44.64536, 43.52338, 44.46138, 43.50631, 44.67692, 43.45663, 43.60871]
max_time = [158.353869047619, 270.5125992063492, 162.2045634920635, 187.9181547619048, 210.2632936507937, 149.127876984127, 219.93125, 186.4375992063492, 26.93293650793651, 167.1896825396825, 221.9734126984127, 221.5076388888889, 274.2358134920635, 36.43611111111111, 42.48700396825397, 171.5013888888889]

fig, ax = plt.subplots(figsize = (100, 100))
bird_tags = ['137441', '126610', '126612', '137439', '137440', '126611', '148822', '148823', '148824', '160365', '160367', '160366', '170144', '170145', '170146', '179524']

for i in range(15,16): 

#FOR Y VECTOR FIELDS
    y_vector_field = pd.read_excel(str(bird_tags[i] + 'yvectorfield.xlsx'))
    #access vector field data
    for j in range(len(y_vector_field)): #x/y axis
        for k in range(len(y_vector_field[0])): #t axis
            #draw a line, for t = 0.5, and plot it, used to show slope of the vector
            vector = y_vector_field.iloc[j][k]
            latitude = math.floor(min_lat[j]) + j*0.5
            time = k*10
            ax.quiver(time, latitude, (time+0.5), (vector*0.5 + latitude))
    

    #plot the vector field
    plt.xlabel('time (weeks)')
    plt.ylabel('latitude')
    plt.xlim([0, math.ceil(max_time[j])])
    plt.ylim([math.floor(min_lat[j])-2, max_lat[j]+2])
    plt.title(str(bird_tags[i]) + " y vector field")
    plt.show()

#FOR X VECTOR FIELDS (Process is exacly the same)


#     x_vector_field = pd.read_excel(str(bird_tags[i] + 'vectorfield.xlsx'))
#     # y_vector_field = pd.read_excel(str(bird_tags[i] + 'yvectorfield.xlsx'))
#     #some error is happening, idk why
#     for j in range(len(x_vector_field)):
#         for k in range(len(x_vector_field[0])):
#             vector = x_vector_field.iloc[j][k]
#             longitude = math.floor(min_long[i]) + j*0.5
#             time = k*10
#             ax.quiver(time, longitude, (time+0.5), (vector*0.5 + longitude))

#     plt.xlabel('time (weeks)')
#     plt.ylabel('longitude')
#     plt.title(str(bird_tags[i]) + " x vector field")
#     plt.show()

    # x_vector_field = pd.read_excel(str(bird_tags[i] + 'vectorfield.xlsx'))