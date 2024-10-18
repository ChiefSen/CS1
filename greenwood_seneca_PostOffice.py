'''
Author:Seneca Greenwood
Description: Gives the cost of several types of parcels and the shipping cost of said parcel to differnt zipcode zones.
Log: 1.0
Bugs: None that are aware
Features: None
Sources: Harriso Servedio
'''


def find_zone(zipcodes):
    #finds the zone when user inputs a value of the zones

    #Args:
        #zipcodes: the numbers that define what zone you are in between variables
    #Return:
            #int: the zone that your are in
    #Raises:
            #ValueError: if input is outside variables

    if zipcodes >= 1 and zipcodes <= 6999:                                       #if users zipcodes are between 10000 and 09999
        return 1                                                                 #give user zone 1
    elif zipcodes >= 7000 and zipcodes <= 19999:                                 #if users zipcodes are between 20000 and 29999
        return 2                                                                 #give user zone 2
    elif zipcodes >= 20000 and zipcodes <= 35999:                                #if users zipcodes are between 30000 and 39999
        return 3                                                                 #give user zone 3
    elif zipcodes >= 36000 and zipcodes <= 62999:                                #if users zipcodes are between 40000 and 49999
        return 4                                                                 #give user zone 4
    elif zipcodes >= 63000 and zipcodes <= 84999:                                #if users zipcodes are between 50000 and 59999
        return 5                                                                 #give user zone 5
    elif zipcodes >= 85000 and zipcodes <= 99999:                                #if users zipcodes are between 60000 and 69999
        return 6                                                                 #give user zone 6
    else:                                                                        #if any other user response is presented
        return "not a valid zip code"                                            #Tells user zipcode is not valid 

def get_package_type(length, hieght, thickness):
    #finds the exact parcel depending on the dimensions that user inputted

    #Args:
        #length, hieght, thickness: the dimensions of the parcels
    #Return:
            #str: the type of parcel

    if length >= 3.5 and length <= 4.25 and hieght >= 3.5 and hieght <= 6 and thickness >= .007 and thickness <= .016:                           #if dimensions fall into category
        return "Regular Post Card"                                                                                                               #Return the category of mailed item to user
    if length >= 4.25 and length <= 6 and hieght >= 6 and hieght <= 11.5 and thickness >= .007 and thickness <= .015:                            #if dimensions fall into category
        return "Large Post Card"                                                                                                                 #Return the category of mailed item to user
    if length >= 3.5 and length <= 6.125 and hieght >= 5 and hieght <= 11.5 and thickness >= .016 and thickness <= .25:                          #if dimensions fall into category
        return "Envolope"                                                                                                                        #Return the category of mailed item to user
    if length >= 6.125 and length <= 24 and hieght >= 11 and hieght <= 18 and thickness >= .25 and thickness <= .5:                              #if dimensions fall into category
        return "Large Envolope"                                                                                                                  #Return the category of mailed item to user
    if length+2*thickness+2*hieght <= 84:                                                                                                        #if dimensi5, 7, .2, 45216, 07245ons fall into category
        return "Package"                                                                                                                         #Return the category of mailed item to user
    if length+2*thickness+2*hieght <= 130:                                                                                                       #if dimensions fall into category
        return "Large Package"                                                                                                                   #Return the category of mailed item to user
    
def find_cost(size, zone):
    #finds the cost of post card and zone
    

    #Args:
        #size: gets the size of the parcel
        #zone: adds the zone payment to the parcel payment depending on what zone
    #Return:
            #int: the cost of the parcel and mailing it

    if size == "Regular Post Card":                                                    #if the size of the mailed item is a "Regular Post Card"
        return .20+.03*zone                                                            #send the cost of item and add it with the cost of mailing it through each zone
    if size == "Large Post Card":                                                      #if the size of the mailed item is a "Large Post Card"
        return .37+.03*zone                                                            #send the cost of item and add it with the cost of mailing it through each zone
    if size == "Envolope":                                                             #if the size of the mailed item is a "Envolope"
        return .37+.04*zone                                                            #send the cost of item and add it with the cost of mailing it through each zone
    if size == "Large Envolope":                                                       #if the size of the mailed item is a "Large Envolope"
        return .60+.05*zone                                                            #send the cost of item and add it with the cost of mailing it through each zone
    if size == "Package":                                                              #if the size of the mailed item is a "Package"
        return 2.95+.25*zone                                                           #send the cost of item and add it with the cost of mailing it through each zone
    if size == "Large Package":                                                        #if the size of the mailed item is a "Large Package"
        return 3.95+.35*zone                                                           #send the cost of item and add it with the cost of mailing it through each zone






def main():

    data = input("Enter data in order length, height, thickness, starting zip code and ending zip code: ")#gives user the option to enter dimensions for the code
    dimensions = data.split(",")                                                       #seperates user's data with commas and inputs it into dimensions
    length = float(dimensions[0])                                                      #takes user's data from index of dimensions and inputs it into length and turns into float
    height = float(dimensions[1])                                                      #takes user's data from index of dimensions and inputs it into height and turns into float
    thickness = float(dimensions[2])                                                   #takes user's data from index of dimensions and inputs it into thickness and turns into float
    starting_zip = int(dimensions[3])                                                  #takes user's data from index of dimensions and inputs it into starting_zip and turns into integer
    ending_zip = int(dimensions[4])                                                    #takes user's data from index of dimensions and inputs it into ending_zip and turns into integer
    start_zone = find_zone(starting_zip)                                               #finds the start zone from user's input
    end_zone = find_zone(ending_zip)                                                   #finds the end zone from user's input
    package_type = get_package_type(length, height, thickness)                         #finds the package type oof user's input of length, height, and thickness
    cost = find_cost(package_type, abs(start_zone-end_zone))                           #finds cost of the package type and the cost to mail between zones
    cost = str('%.2f'%cost).lstrip("0")                                                #removes leading zero in cost 
    print(cost)                                                                        #prints the cost of the package
  
            

            







main()
