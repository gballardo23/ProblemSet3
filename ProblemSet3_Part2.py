# Problem Set 3 - Part 2
# Gabi Ballardo
# 10/14/2022

#%% Task 4.1 ---------------------------------------

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2 

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)


#%% Task 4.3

#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for headerLineString in lineList[1:]:
    #Split the data into values
    data_line = headerLineString.split(",")
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = data_line[mmsi_idx]
    #Extract the fleet value
    fleet = data_line[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
    
#%% Task 4.4

#Create vessel ID variable and assign the value 258799000 to it
vesselID = 258799000

#Lookup the fleet value for the vessel with MMSI=vesselID value in the dictionary
vesselDict[fleet, vesselID]

#Change vesselID to a string
str(vesselID)

#Print the statement: Vessel # 258799000 flies the flag of Norway
print("Vessel #" + vesselID + " flies the flag of Norway")
