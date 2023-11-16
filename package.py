# Student ID: 011194327
# Author: Ronald Bodnar
# WGU C950 Data Structures and Algorithms II

import datetime

class Package:
    
    def __init__(self, id, street, city, state, zip, deadline, weight, notes, status, truckNumber, departureTime, deliveryTime):
        self.id = id
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departureTime = departureTime
        self.deliveryTime = deliveryTime
        self.truckNumber = truckNumber

    def __str__(self):
        return '%-5s%-40s%-18s%-8s%-8s%-12s%-12s%-12s%-18s%-15s%-13s' % (self.id, self.street, self.city, self.state, self.zip, self.deadline, self.weight, self.status, self.departureTime, self.deliveryTime, self.truckNumber)
    
    # Update package information to reflect the details of the package at the given time.
    def update(self, time):
        # Show the package's status at the given time.
        if time >= self.deliveryTime:
            self.status = "Delivered"
        elif time > self.departureTime:
            self.status = "En Route"
        else:
            self.status = "At Hub"
            
        # Show the delivery address for package 9 at the given time.
        if self.id == 9:
            self.street = "410 S State St" if time > datetime.timedelta(hours=10, minutes=20) else "300 State St"
            self.zip = "84111" if time > datetime.timedelta(hours=10, minutes=20) else "84103"