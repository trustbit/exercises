import sys

if len(sys.argv) == 2:
    INPUT = sys.argv[1]
else:
    print("Using default input")
    INPUT = 'AABABBAB'

print(f"Deliver {INPUT}")

TIME = 0
FACTORY = list(INPUT)
A = []
B = []
PORT = []


def work_done():
    return len(A) + len(B) == len(INPUT)


WORLD = {'FACTORY': FACTORY, 'PORT': PORT, 'A': A, 'B': B}
MAP = {
    ('TRUCK', 'FACTORY', 'A'): ('PORT', 1),
    ('TRUCK', 'FACTORY', 'B'): ('B', 5),
    ('TRUCK', 'PORT', None): ('FACTORY', 1),
    ('TRUCK', 'B', None): ('FACTORY', 5),
    ('SHIP', 'PORT', 'A'): ('A', 4),
    ('SHIP', 'A', None): ('PORT', 4),
}


class Transport:
    def __init__(self, loc, kind):
        self.loc = loc
        self.kind = kind
        self.eta = 0
        self.cargo = None

    def move(self):
        if self.eta > TIME:
            # print(f"{self.kind} arrives to {self.loc} in {self.eta-TIME}")
            return

        place = WORLD[self.loc]
        if self.cargo:
            place.append(self.cargo)
            print(f'  {self.kind} drops {self.cargo} at {self.loc}')
            self.cargo = None
        else:
            if place:
                self.cargo = place.pop(0)
                print(f'  {self.kind} picks {self.cargo} at {self.loc}')

        plan = (self.kind, self.loc, self.cargo)

        if plan in MAP:
            dest, eta = MAP[plan]
            self.loc = dest
            self.eta = eta + TIME
        else:
            # print(f'{self.kind} has no plan for {plan}')
            pass


transport = [Transport('FACTORY', 'TRUCK'), Transport('FACTORY', 'TRUCK'), Transport('PORT', 'SHIP')]

while True:
    print(TIME)

    for t in transport:
        t.move()

    if work_done():
        print("  DONE")
        break
    TIME += 1
