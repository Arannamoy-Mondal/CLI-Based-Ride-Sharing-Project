from datetime import datetime
class Ride:
    def __init__(self,start_location,end_location):
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fare=None

    def set_driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time=datetime.now()
    def end_ride(self):
        self.end_time=datetime.now()
        self.rider.wallet-=self.estimated_fare
        self.driver.wallet+=self.estimated_fare

    def __repr__(self):
        return f'Ride details:\nStart Location To End Location: {self.start_location} -- {self.end_location}\nEstimate fare: {self.estimated_fare}'

class RideRequest:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location

class RideMatching:
    def __init__(self,drivers):
        self.available_drivers=drivers
    
    def find_driver(self,ride_request):
        if len(self.available_drivers) > 0:
            print("Looking for drivers")
            driver=self.available_drivers[0]
            ride=Ride(ride_request.rider.start_location,ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        

# print(datetime.now()) 