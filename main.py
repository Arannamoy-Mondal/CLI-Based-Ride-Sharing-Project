from ride import Ride,RideMatching,RideRequest,RideSharing
from users import Rider,Driver
from vehicle import Car,Bike


tourMate=RideSharing("TourMate")
rider1=Rider("Rider1","xyz",1,"MaryLand",10)
driver1=Driver("Driver1","xyz",2,"MaryLand")
tourMate.add_driver(driver1)
tourMate.add_rider(rider1)
rider1.request_ride(tourMate,"Uttara","car")
rider1.show_current_ride()
driver1.reach_destination(rider1.current_ride)
print(tourMate)