import pandas as pd
import math

def calculate_distances(lat, lng, score, contact):
    center_data = pd.read_csv("total_database1.csv")
    distance_list = []
    for i in range(len(center_data.index)):
        x1 = center_data["latitudes"][i]
        y1 = center_data["longitudes"][i]
        minboi = math.sqrt((lat-x1)*(lat-x1) + (lng-y1)*(lng-y1))
        distance_list.append(minboi)

    center_data['minimum distance'] = distance_list
    #print(center_data)


    center_data.sort_values(by=['minimum distance'], inplace=True)

    if score > 7:
        statement = "It is urgent that you get professional help. You are being directed to hospitals and doctors near you."
        admit_locations = center_data.loc[center_data['Doctor Consultation AND ADMIT'] == 'Y']
        admits_list = admit_locations.values.tolist()
        final_list=admits_list

    elif 7 >= score >= 6:
        statement = "Must do a professional covid-19 test.You may be infected with covid-19. We will be accessing your devices information to help you find the nearest open covid testing center. "
        testing_locations = center_data.loc[center_data['testing'] == 'Y']
        testing_list = testing_locations.values.tolist()
        final_list=testing_list

    elif 5 >= score >= 4:
        statement = "You might be infected with covid-19. You need to do a take-at-home test.  We will be accessing your devices information to help you find the nearest store which will sell take-at-home covid tests"
        home_locations = center_data.loc[center_data['home testing'] == 'Y']
        home_list = home_locations.values.tolist()
        final_list=home_list

    elif 0 < score <= 3:
        statement = "you must isolate yourself for 5 days, if no more symptoms then you are not infected. We will be accessing your devices information and providing you with information regarding where resources such as masks are available. "
        mask_locations = center_data.loc[center_data['Masks'] == 'Y']
        mask_list = mask_locations.values.tolist()
        final_list = mask_list
    
    else:
        statement = "Isolate for 7 days if no more symptoms then you are not infected"
        final_list = 'None'

    if contact == 1:
        statement = "You must Isolate for 14 days and do a covid-19 test.We will be accessing your devices information to help you find the nearest open covid testing center"

    return [statement, final_list, distance_list]



lat=-16.63007
lng=-71.06416            
score=8
contact=1

new__1 = calculate_distances(lat, lng, score, contact)

for i in new__1:
    print(i)
