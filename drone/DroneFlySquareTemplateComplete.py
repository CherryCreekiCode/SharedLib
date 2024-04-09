from drone.EasyTelloMocker import EasyTelloMocker

DEBUG = True
myDrone = EasyTelloMocker(debug=DEBUG)


def makeTurn(turn):
    if turn == 'l':
        for i in range(4):
            myDrone.forward(150)
            myDrone.ccw(90)
    elif turn == 'r':
        for i in range(4):
            myDrone.forward(150)
            myDrone.cw(90)


myDrone.takeoff()

if battery_status < 75:
    makeTurn('l')
else:
    makeTurn('r')

myDrone.land()
