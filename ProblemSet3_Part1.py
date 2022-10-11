#%%
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = '"Mt. McKinley"'
elevation = "20322"

print(mountain + ", formerly \nknown as "+ nickname +" \nis " + elevation + "' above sea level." )
#%%

#%%
#Task 2 -- Lists and Iteration -------------------------

data_folder = "W:\859_data\tri_state"
data_list = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]
user_item = "streams.shp"
data_list.append(user_item)
print(data_list)

for item in data_list:
    data_list = [data_folder + item]
    print(data_list)
    
#%%
#Task 3 ------------------------------------------------------------

# create an empty list variable
user_numbers = []

# iterate process three times
user_input = input("Enter an integer: ")
for user_input in range(3):
    user_numbers.append(user_input)
    print(user_numbers.sort())
    
    

