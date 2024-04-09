# from easytello import tello
from drone.EasyTelloMocker import EasyTelloMocker
import sys


DEBUG = True

"""
    get_min_temp_loc
        input: Array of (temperature, location) tuples
        return: The index location of the minimum temperature
        
"""

def get_min_temp_loc(temperatures):
    min_temp = sys.maxsize
    location = -1
    for temp, loc in temperatures:
        if temp < min_temp:
            min_temp = temp
            location = loc
    return location


"""
    get_max_temp_loc
        input: Array of (temprature, location) tuples
        return: The index location of the maximum temperature

"""

def get_max_temp_loc(temperatures):
    max_temp = -sys.maxsize - 1
    location = -1
    for temp, loc in temperatures:
        if temp > max_temp:
            max_temp = temp
            location = loc
    return location


"""
    collect_temp_data
        This function iterates over the checkpoints array and travels the distance (cm)
        defined at that index
        return: Returns the index location of the drone's last position
"""

def collect_temp_data():
    loc = -1
    for checkpoint in checkpoints:
        myDrone.wait(3)
        loc += 1
        temperature_list.append((myDrone.get_temp(), loc))
        if checkpoint != 0:
            myDrone.forward(checkpoint)
        print("Location = ", loc)
    return loc


"""
    goto_location
        Calculate the direction and number of hops between the start and end index location 
        input: start is the current index location of the drone
                end is the target index we want the drone to move to
        return: Returns the index location of the drone's last position
        
        Ex 1.
            checkpoints = [0, 500, 500]
                    index  0,   1,    2  
            start = 2, end = 0
            Drone moves backward the value of the indices 1 (500cm), and 0 (0cm) 
"""

def goto_location(start, end):
    hopnum = start - end
    print("Current location: {} | Number of HOPs: {}".format(start, hopnum))
    if hopnum < 0:
        hopnum = abs(hopnum)
        print("Forward ", hopnum)
        for i in range(hopnum):
            if checkpoints[i] >= 20:
                myDrone.forward(checkpoints[i])
    else:
        hopnum = abs(hopnum)
        print("Backward ", hopnum)
        for i in reversed(range(hopnum + 1)):
            if checkpoints[i] >= 20:
                myDrone.back(checkpoints[i])

    return end


# Beginning of the program
# myDrone = tello.Tello()
myDrone = EasyTelloMocker(debug=DEBUG)

checkpoints = [0, 500, 500]
temperature_list = []
print(myDrone.get_battery())

# Begin movement
myDrone.takeoff()

# Collect Temperature data from the locations
current_location = collect_temp_data()
min_location = get_min_temp_loc(temperature_list)
print(temperature_list)
myDrone.land()
myDrone.wait(2)

myDrone.takeoff()
current_location = goto_location(current_location, get_min_temp_loc(temperature_list))
myDrone.land()
myDrone.wait(3)

myDrone.takeoff()
goto_location(current_location, get_max_temp_loc(temperature_list))
myDrone.land()
