# Student ID: 011194327
# Author: Ronald Bodnar
# WGU C950 Data Structures and Algorithms II

import csv
import datetime

from truck import Truck
from package import Package
from hashmap import HashMap

# Initialize the hashmap for the list of packages.
packages = HashMap() 

# Load all necessary data from CSV files
# O(n) space-time complexity
def load_data():
    # Set the variable scope for use outside of this function
    global addressData, distanceData
    
    # Load the address data
    with open("csv/address_data.csv") as csvData:
        addressData = csv.reader(csvData)
        addressData = list(addressData)
    
    # Load the distance data
    with open("csv/distance_data.csv") as csvData:
        distanceData = csv.reader(csvData)
        distanceData = list(distanceData)
    
    # Load the package data
    with open('csv/package_data.csv') as csvData:
        packageData = csv.reader(csvData, delimiter=',')
        
        # Iterate through packages to create Package instances
        for package in packageData:
            id = int(package[0])
            street = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            weight = package[6]
            notes = package[7]
            
            # Construct the Package instance
            package = Package(id, street, city, state, zip, deadline, weight, notes, "At Hub", 0, None, None)
            
            # Add the created Package instance to the packages hashmap
            packages.insert(id, package)

#finds the minimum distance for the next address
# O(n) space-time complexity
def find_address(address):
    for row in addressData:
        if address in row[2]:
           return int(row[0])

# Extracts the distance between two addresses
# O(1) space-time complexity
def distance_between(address1, address2):
    distance = distanceData[address1][address2]
    if distance == '':
        distance = distanceData[address2][address1]
    return float(distance)

# Begins the process of delivering packages and utilizes the Nearest Neighbor Algorithm for efficient routing.
# O(n^2) space-time complexity
def deliver_packages(truck):
    # Stores a list of packages that are yet to be delivered.
    packagesToDeliver = []
    
    # Iterate through the packages on the truck to populate the packagesToDeliver list.
    for packageId in truck.packages:
        package = packages.search(packageId)
        package.truckNumber = truck.number
        packagesToDeliver.append(package)

    # Clear the truck's packages so they can be re-added in the order which they are delivered.
    truck.packages.clear()
    
    # Continually perform the Nearest Neighbor algorithm until all packages have been delivered.
    while len(packagesToDeliver) > 0:
        nextPackage = None
        distanceToNextAddress = 2000
        
        # Iterate through the remaining packages to find the closest neighbor.
        for package in packagesToDeliver:
            # If a package is found to be closer than previous packages, update distanceToNextAddress and set package to nextPackage.
            if distance_between(find_address(truck.location), find_address(package.street)) <= distanceToNextAddress:
                distanceToNextAddress = distance_between(find_address(truck.location), find_address(package.street))
                nextPackage = package
                
        # Add the next package to be delivered to the truck's package list.
        truck.packages.append(nextPackage.id)
        
        # Remove the next package from the packagesToDeliver list.
        packagesToDeliver.remove(nextPackage)
        
        # Update the truck's location, miles driven, and current time.
        truck.location = nextPackage.street
        truck.milesDriven += distanceToNextAddress
        truck.currentTime += datetime.timedelta(hours=(distanceToNextAddress / truck.speed))
        
        # Update the package details to reflect the delivered status and departure and delivery times.
        nextPackage.status = "Delivered"
        nextPackage.deliveryTime = truck.currentTime
        nextPackage.departureTime = truck.departureTime

# Initialize the command-line interface for user input and provide daily route information.
# O(n) space-time complexity
def initialize_ui():
    # Populate a list with the total miles driven for each truck.
    totalMilesDriven = lambda : [truck.milesDriven for truck in trucks]
    totalMilesDriven = sum(totalMilesDriven())
    
    # Populate a list with the total number of packages delivered from each truck.
    totalPackagesDelivered = lambda : [len(truck.packages) for truck in trucks]
    totalPackagesDelivered = sum(totalPackagesDelivered())
    
    print(("=" * 10), "Western Governors University Parcel Service (WGUPS)", ("=" * 10))
    
    print("Today's route of %s packages was completed in %s miles"
          % (totalPackagesDelivered, totalMilesDriven))
    
    print("\tTruck 1: %s miles, %s packages\n\tTruck 2: %s miles, %s packages\n\tTruck 3: %s miles, %s packages"
          % (round(trucks[0].milesDriven, 2), len(trucks[0].packages),
             round(trucks[1].milesDriven, 2), len(trucks[1].packages),
             round(trucks[2].milesDriven, 2), len(trucks[2].packages)))

    print("\nThis WGUPS reporting tool can provide reports for the following options:")
    print("\t1. View a snapshot of all package deliveries for the day.")
    print("\t2. View a snapshot of package details for a specific time.")
        
    # Prompt the user to enter a report type (1 or 2).
    reportType = input("\nPlease enter the number of the report you would like to view: ")
        
    # Ensure that the user enters a valid report type (only 1 or 2 are accepted).
    # If not, prompt the user to enter a valid report type to view.
    while not reportType in ["1", "2"]:
        reportType = input("\nPlease enter the number (1 or 2) of the report you would like to view. ")
            
    # Output complete snapshot of all trucks and deliveries
    if reportType == "1":
        print('%-5s%-40s%-18s%-8s%-8s%-12s%-12s%-12s%-18s%-15s%-13s' % ("ID", "Street", "City", "State", "Zip", "Deadline", "Weight", "Status", "Departure Time", "Delivery Time", "Truck Number"))
        # Print delivery details for all 40 packages at the end of the day.
        for id in range(1, 41):
            package = packages.search(id)
            print(package)
            
    # Output detailed snapshot of package details for a specified time.
    else:
        # Prompt the user to enter a time for which they'd like to see the status of package(s).
        desiredTime = input("Please enter a time for your snapshot using military time (0800 to 2400): ")
            
        # Ensure that the desiredTime input from the user is a valid military time with 4 numeric digits
        # and is within 0800 and 2400 hours.
        # If not, prompt the user to enter a valid military time string.
        while not desiredTime.isnumeric() or len(desiredTime) != 4 or int(desiredTime) < 800 or int(desiredTime) > 2400:
            desiredTime = input("You must enter a valid time using military format. Please enter a time: ")
                
        # Extract the hours and minutes from the desiredTime input.
        hours = desiredTime[0:2]
        minutes = desiredTime[2:4]
        
        # Reassign desiredTime to a timedelta Object.
        desiredTime = datetime.timedelta(hours=int(hours), minutes=int(minutes));
        
        # Prompt the user to enter a package ID if they would like to view a specific package.
        packageId = input("Please enter a package ID (1 - 40) or press enter to view all packages: ")
        
        # Ensure that the package id input from the user is either blank or a number within the range of 1-40
        # If not, prompt the user to enter a valid package ID.
        while packageId != "" and (not packageId.isnumeric() or int(packageId) < 1 or int(packageId) > 40):
            packageId = input("Please enter a valid package ID (1 - 40) or press enter to view all packages: ")
            
        print('%-5s%-40s%-18s%-8s%-8s%-12s%-12s%-12s%-18s%-15s%-13s' % ("ID", "Street", "City", "State", "Zip", "Deadline", "Weight", "Status", "Departure Time", "Delivery Time", "Truck Number"))
        
        # If no package ID was entered, display all package details for the specified time.
        if packageId == "":
            for id in range(1, 41):
                package = packages.search(id)
                package.update(desiredTime)
                print(package)
                
        # If a package ID was entered, display just the details for that package.
        else:
            package = packages.search(int(packageId))
            package.update(desiredTime)
            print(package)
            

# Load the data from CSV files.
load_data()

# Set up trucks with manual loading of packages and departure times to meet constraints.
trucks = [
    Truck(1, 18, "4001 South 700 East", datetime.timedelta(hours=8), [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]),
    Truck(2, 18, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20), [3, 12, 17, 18, 21, 22, 23, 24, 27, 35, 36, 38, 39]),
    Truck(3, 18, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5), [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 26, 28, 32, 33])
]

# Deliver packages using trucks 1 & 2. 
deliver_packages(trucks[0])
deliver_packages(trucks[1])

# Deliver packages using truck 3 once either truck 1 or 2 has returned to the Hub.
trucks[2].departureTime = min(trucks[0].currentTime, trucks[1].currentTime)
deliver_packages(trucks[2])

# Begin the command-line interface to allow the user to view package/delivery snapshots.
initialize_ui()