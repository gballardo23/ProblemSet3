# Problem Set 3 - Part 1
# Gabi Ballardo
# 10/14/2022

#%% Task 1 --  Python syntax & string manipulation ----------------------------

#Create string variables 

mountain = "Denali"
#Use two sets of quotes so that quotes will appear when printed
nickname = '"Mt. McKinley"'
elevation = "20322"

#Print statement into 3 separate lines using the above variables
    #Use \n to start a new line and add quotes around words to indicate strings
print(mountain + ", formerly \nknown as "+ nickname +" \nis " + elevation + "' above sea level." )


#%% Task 2 -- Lists and iteration ---------------------------------------------

#Assign data_folder variable to the string object that reads “W:\859_data\tri_state"
data_folder = "W:\859_data\\tri_state"
#Create a list object containing string objects: roads.shp, road_types.dbf, naip_imagery.tif
data_list = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]
#Assign user_item variable and set it to the string “streams.shp”
user_item = "streams.shp"
#Add the user_item string object to the data_list list
data_list.append(user_item)
print(data_list)

#Concatenate data_folder string with each item in the data_list
for item in data_list:
    #Use '\\' to get rid of double \\ at the beginning of the file name
    print(data_folder+'\\'+item)
    
#%% Task 3 -- Lists and iteration continued  ----------------------------------

#Create an empty list variable: user_numbers
user_numbers = []

#Iterate the following process three times: Ask user to input integer and add to list

#Range(0,3) indicates the number of times to iterate
for user_input in range(0,3):
    #Use int function to turn the "Enter an integer:" string into an integer
    user_input = int(input("Enter an integer: "))
    #Add user integer inputs to the user_numbers list
    user_numbers.append(user_input)
    
#Sort the user_numbers list in ascending order
user_numbers.sort()
#Print the largest number/the last number in the list
print(user_numbers[-1])

#%% Task 3 -- Challenge -------------------------------------------------------
#Repeat the same code/steps as the last code cell with minor modifications

#Create an empty list variable: userNumbers (different variable name so that the list isn't overwritten)
userNumbers = []

#Iterate the following process three times: Ask user to input integer and add to list

#Range(0,3) indicates the number of times to iterate
for user_input in range(0,3):
    #Use int function to turn the "Enter an integer:" string into an integer
    user_input = int(input("Enter an integer: "))
    #Add user integer inputs to the user_numbers list
    userNumbers.append(user_input)
    
#Sort userNumbers list in descending order
userNumbers.sort(reverse=True)
#Print the entire contents of the userNumbers list
print(userNumbers)



