# Problem Set 3 - Part 2
# Gabi Ballardo
# 10/14/2022

# Lists, dictionaries, string manipulation, and iteration

#%% Task 4.1 -- Reading in the data and displaying the column headers ---------

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

#%% Task 4.2 -- Splitting the header string into a list of column names and extracting index values

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)


#%% Task 4.3 --  Iterating through the data lines and adding values to a dictionary
# NOTE: fleet is returning Malta only, but not sure why (Task 5 returns incorrect output consequently)

#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for i in range(1, len(lineList)):
    #Split the data into values
    data_line = lineList[i].split(',')
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = data_line[mmsi_idx]
    #Extract the fleet value
    fleet = data_line[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
    
#%% Task 4.4 -- Using the dictionary

#Create vessel ID variable and assign the value 258799000 to it
vesselID = "258799000"

#Lookup the fleet value for the vessel with MMSI=vesselID value in the dictionary
print(vesselDict[vesselID])

#Print the statement: Vessel # 258799000 flies the flag of Norway
print("Vessel #" + vesselID + " flies the flag of " + vesselDict[vesselID])

#%% Task 5

#Create a Python file object, i.e., a link to the file's contents
loitering_fileobj = open(file='loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
loiter_lineList = loitering_fileobj.readlines()

#Release the link to the file objects (now that we have all its contents)
loitering_fileobj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerlinestring"
headerlinestring2 = loiter_lineList[0]

#Print the contents of the headerLine
print(headerlinestring2)

#Split the string into data line
Data_line = headerlinestring2.split(",")

#List the index of the transshipment_mmsi, starting_latitude, ending_latitude and starting_longitude values
trans_mmsi_idx = Data_line.index('transshipment_mmsi')
start_lat_idx = Data_line.index('starting_latitude')
end_lat_idx = Data_line.index('ending_latitude')
start_long_idx = Data_line.index('starting_longitude')

#Create Boolean variable
requirements = False

#Iterate through all lines (except the header) in the data file:
for i in range(1, len(loiter_lineList)):
    #Split the list into data items
    split_dataset = loiter_lineList[i].split(',')
    tran_mmsi = split_dataset[trans_mmsi_idx]
    st_lat = float(split_dataset[start_lat_idx])
    end_lat = float(split_dataset[end_lat_idx])
    st_lon = float(split_dataset[start_long_idx])
    #Determine whether event passes equator and if coordinates fall between 165 and 170
    if st_lat < 0 and end_lat > 0:
        if st_lon < 170 and st_lon > 165:
            requirements = True
            fleet = vesselDict[tran_mmsi]
            print("Vessel #" + tran_mmsi + " flies the flag of " + fleet)
            
#Print if no vessels met criteria
if requirements == False:
    print("No vessels met criteria")
    

# NOTE: In Task 4.3, fleet returned Malta, which interferred with Task 5 outputs
    
    
