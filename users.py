from abc import ABC,abstractmethod
from ride import RideRequest,RideMatching,RideSharing
class User(ABC):
    def __init__(self,name,email,id):
        # super().__init__()
        self.name=name
        self.email=email
        self.id=id
        self.wallet=0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, id,current_location,initial_amount):
        super().__init__(name, email, id)
        self.current_ride=None
        self.wallet=initial_amount
        self.current_location=current_location

    def display_profile(self):
        print(f"Rider: {self.name} and email: {self.email}")
    
    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
        else:
            print("Must be greater than 0.")
    def update_location(self,current_location):
        self.current_location=current_location

    def request_ride(self,ride_sharing,destination,vehicle_type):
        ride_request=RideRequest(self,destination)
        ride_matching=RideMatching(ride_sharing.drivers)
        ride=ride_matching.find_driver(ride_request,vehicle_type)
        # ride=ride_matching.find_driver(ride_request)
        self.current_ride=ride
        print("Yay!!! We got a ride.")
        
    def show_current_ride(self):
        print(f"Current ride: {self.current_ride}")


class Driver(User):
    def __init__(self, name, email, id,current_location):
        super().__init__(name, email, id)
        self.current_location=current_location
        self.wallet=0

    def display_profile(self):
        print(f"Driver name: {self.name}")
    
    def accept_ride(self,ride):
        ride.start_ride()
        ride.set_driver(self) # driver object
    def reach_destination(self,ride):
         ride.end_ride()