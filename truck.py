# Student ID: 011194327
# Author: Ronald Bodnar
# WGU C950 Data Structures and Algorithms II

class Truck:
    
    def __init__(self, number, speed, location, departureTime, packages):
        self.number = number
        self.speed = speed
        self.location = location
        self.departureTime = departureTime
        self.packages = packages
        
        self.milesDriven = 0.0
        self.currentTime = departureTime