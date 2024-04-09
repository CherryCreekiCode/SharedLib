from easytello import tello
import time
import random

class EasyTelloMocker:


    def __init__(self, debug):
        self.random_values = [76.3, 45.6, 38.1, 22.7, 16.0]
        self.debug = debug
        if debug:
            self.drone = self
        else:
            self.drone = tello.Tello()

    def __str__(self):
        return f"{self.name}({self.age})"

    def takeoff(self):
        if self.debug:
            print("Drone is Taking Off")
        else:
            return self.drone.takeoff()

    def land(self):
        if self.debug:
            print("Drone is Landing")
        else:
            return self.drone.land()

    def get_battery(self):
        if self.debug:
            print("Getting Battery")
            return random.choice(self.random_values)
        else:
            return self.drone.get_battery()

    def wait(self, s):
        if self.debug:
            print("Drone is waiting")
            time.sleep(s)
        else:
            self.drone.wait(s)

    def forward(self, distance):
        if self.debug:
            print("Drone is moving forward:", distance)
        else:
            return self.drone.forward(distance)

    def back(self, distance):
        if self.debug:
            print("Drone is moving backward:", distance)
        else:
            return self.drone.back(distance)

    def get_temp(self):
        if self.debug:
            return random.choice(self.random_values)
        else:
            return self.drone.get_temp()
