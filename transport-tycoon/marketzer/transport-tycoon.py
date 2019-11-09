import sys
from collections import deque


class Transport:
    def __init__(self, loc):
        self.destination = loc
        self.waypoint = loc
        self.duration = 0
        self.location = loc


def print_usage():
    print('Usage: ', sys.argv[0], ' route')


def getWaypointWithDuration(dest, location='Factory'):
    if dest == 'A':
        if location == 'Factory':
            return 'Port', 1
        if location == 'Port':
            return 'A', 4
    if dest == 'B':
        return 'B', 5

    if dest == 'Factory':
        if location == 'Port':
            return 'Factory', 1
        return 'Factory', 5

    if dest == 'Port':
        return 'Port', 4


if len(sys.argv) == 1:
    print_usage()
    sys.exit(1)

print('Calculating time for route: ', list(sys.argv[1]))

factory = deque(sys.argv[1])
port = deque()
trucks = []
for i in range(2):
    trucks.append(Transport('Factory'))

ships = [Transport('Port')]
time = 0

while True:
    increaseTime = False

    for idx in range(len(trucks)):
        truck = trucks[idx]
        if truck.destination == 'Factory' and len(factory) == 0:
            continue

        if truck.duration == 0:
            truck.location = truck.waypoint
            if truck.waypoint == 'Port':
                port.append(truck.destination)
            if truck.destination != 'Factory':
                truck.destination = 'Factory'
                if len(factory) == 0:
                    continue
            else:
                truck.destination = factory.popleft()

            truck.waypoint, truck.duration = getWaypointWithDuration(truck.destination, truck.location)

        truck.duration -= 1
        increaseTime = True

    for idx in range(len(ships)):
        ship = ships[idx]
        if ship.destination == 'Port' and len(port) == 0:
            continue

        if ship.duration == 0:
            ship.location = ship.waypoint
            if ship.destination != 'Port':
                ship.destination = 'Port'
                if len(port) == 0 and increaseTime is False:
                    continue
            else:
                ship.destination = port.popleft()

            ship.waypoint, ship.duration = getWaypointWithDuration(ship.destination, ship.location)

        ship.duration -= 1
        increaseTime = True

    if not increaseTime:
        break

    time += 1

print('Time: ', time)
