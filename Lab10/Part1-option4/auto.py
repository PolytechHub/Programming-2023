from datetime import timedelta
import math

class Auto():
    '''Car class in one-dimensional space'''
    def __init__(self, color='red', brand='mercedes', 
                drive_type='front', mileage=10000,
                cost=100000, newcost=1000000, gps=[337, 1],
                maxspeed=250, engine_type='petrol',
                fuel_consumption=0.1, remaning_fuel=100, 
                service_interval=timedelta(days=360)):
        self.color = color
        self.brand = brand
        self.drive_type = drive_type
        self.mileage = mileage
        self.cost = cost
        self.newcost = newcost
        self.gps = gps
        self.maxspeed = maxspeed
        self.engine_type = engine_type
        self.remaning_fuel = remaning_fuel
        self.fuel_consumption = fuel_consumption
        self.service_interval = service_interval

    def go_to_city(self, gps):
        '''Checking the ability to get to the city without refueling'''
        distance = self.distance_to_point(gps)
        return self.remaning_fuel / self.fuel_consumption >= distance
    
    def distance_to_point(self, gps):
        '''Distance in kilometers from the current point to this point'''
        # Мега костыль, не делайте так
        pointX, pointY = gps
        def distance(x1, y1, x2, y2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        return distance(self.gps[0], self.gps[1], pointX, pointY)
    
    def cost_of_trip(self, gps, fuel_cost):
        '''The price of a trip in dollars from the current point to this point, taking into account this fuel price'''
        return self.distance_to_point(gps) * self.fuel_consumption * fuel_cost
    
    def time_of_trip_with_max_speed(self, gps):
        '''Time from the current point to the given point at maximum speed'''
        return self.distance_to_point(gps) / self.maxspeed
    
    def price_loss(self):
        '''Loss of price from the moment of purchase'''
        return self.newcost - self.cost