from dataclasses import dataclass
from enum import Enum


class MoveMethod(Enum):
    GROUND = 1
    WATER = 2
    AIR = 3


class TransportState(Enum):
    FULL = 1
    EMPTY = 2


IN_THE_WAY = "in the way"


@dataclass
class Warehouse:
    name: str
    cargoids: [int]


@dataclass
class Route:
    source: str
    dest: str
    time: int
    move_method: MoveMethod

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Route):
            return self.source == other.source and self.dest == other.dest and self.move_method == other.move_method
        return NotImplemented

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        x = self.__eq__(other)
        if x is not NotImplemented:
            return not x
        return NotImplemented


@dataclass
class Cargo:
    id: int
    start: str
    end: str
    current_state: str
    current_transport: str


@dataclass
class TransportState:
    name: str
    move_method: MoveMethod
    cargoid: int
    start_time: int
    duration: int
    start: str
    end: str
    current: str


    def next_step(self, current_time, warehouses, cargos, routes):
        if self.start_time + self.duration > current_time:
            print("- {} drove  CARGO-{}[{} of {} through]".format(self.name, self.cargoid,
                                                   current_time - self.start_time,
                                                   self.duration))
            return

        self.current = self.end

        # delivered
        if self.cargoid >= 0:
            current_warehouse=list(filter(lambda w: w.name == self.end, warehouses))[0]
            current_warehouse.cargoids.append(self.cargoid)

            print("- {} delivered CARGO-{}".format(self.name, self.cargoid))
            current_cargo = \
                list(filter(lambda c: c.id == self.cargoid, cargos))[0]
            current_cargo.current_state = self.end
            current_cargo.current_transport = ""
            current_cargo.blocked_by=""
            self.cargoid = -1


        # if this wWH has cargos for the transport
        current_warehouse = \
        list(filter(lambda w: w.name == self.current, warehouses))[0]

        for ci in current_warehouse.cargoids:
            cargo = list(filter(lambda c: c.id == ci, cargos))[0]
            if cargo.end == cargo.current_state:
                continue

            candidates = find_next_stop_point_by_way(routes, current_warehouse.name,
                                                     cargo.end,
                                                     self.move_method, 1)

            if len(candidates) == 0:
                continue

            min_cand_val = 10000000
            min_cand = []
            for can in candidates:
                val = can[0].time
                if val < min_cand_val:
                    min_cand_val = val
                    min_cand = can

            self.cargoid = cargo.id
            self.start_time = current_time
            self.duration = min_cand[0].time
            self.start = min_cand[0].source
            self.end = min_cand[0].dest
            self.current = IN_THE_WAY
            current_warehouse.cargoids.pop(0)
            cargo.current_state = IN_THE_WAY
            cargo.current_transport = self.name
            print(
                "- {} take CARGO-{} from {} to {}".format(self.name, self.cargoid,
                                                        self.start, self.end))
            return


        # find other WHs where we can found cargos for the transport
        for w in warehouses:

            if w.name == self.current:
                continue

            distance = warehouses_connected(routes, w.name, self.current,
                                            self.move_method)
            if distance == 0:
                continue

            for ci in w.cargoids:
                cargo = list(filter(lambda c: c.id == ci, cargos))[0]
                candidates = find_next_stop_point_by_way(routes, self.current,
                                                         cargo.end,
                                                         self.move_method,
                                                         distance + 1)

                if len(candidates) == 0:
                    continue

                min_cand_val = 10000000
                min_cand = []
                for can in candidates:
                    val = can[0].time
                    if val < min_cand_val:
                        min_cand_val = val
                        min_cand = can

                self.cargoid = -1
                self.start_time = current_time
                self.duration = min_cand[0].time
                self.start = min_cand[0].source
                self.end = min_cand[0].dest
                self.current = IN_THE_WAY
                print("{} rides from {} to {}".format(self.name, self.start,
                                                      self.end))

                return

        print("- {} is resting".format(self.name))


def find_next_stop_point_by_way(routes, current, end, method, move_step):
    candidates = []
    for r in routes:
        if r.source != current:
            continue

        if move_step > 0 and r.move_method != method:
            continue

        if r.dest == end:
            candidates.append([r])
            continue

        newRoutes = list(
            filter(lambda x: x != r, routes))
        if move_step<=1:
            newRoutes = list(
                filter(lambda x: x != Route(r.dest,r.source,r.time,r.move_method), routes))

        res = find_next_stop_point_by_way(newRoutes, r.dest, end, method,
                                          move_step - 1)
        if len(res) == 0:
            continue

        for inner_r in res:
            inner_r.insert(0, r)
            candidates.append(inner_r)

    return candidates


def warehouses_connected(routes: [], w1: str, w2: str,
                         method: MoveMethod) -> int:
    for r in routes:
        if r.move_method != method:
            continue

        if r.source != w1:
            continue

        if r.dest == w2:
            return 1

        newRoutes = list(
            filter(lambda x: x != r and x != Route(r.dest, r.source, r.time,
                                                   r.move_method), routes))
        in_r = warehouses_connected(newRoutes, r.dest, w2, method)
        if in_r > 0:
            return in_r + 1

    return 0


input_distance = [
    {"B": "Factory", "E": "Port", "D": 1, "T": MoveMethod.GROUND},
    {"B": "Factory", "E": "B", "D": 5, "T": MoveMethod.GROUND},
    {"B": "Port", "E": "A", "D": 4, "T": MoveMethod.WATER},
]

cargo_list = "AABABBAB"

if __name__ == "__main__":
    routes = []
    cargos = []
    warehouses = [
        Warehouse("Factory", []),
        Warehouse("Port", []),
        Warehouse("B", []),
        Warehouse("A", []),
    ]
    transports = [
        TransportState("Car_1", MoveMethod.GROUND, -1, 0, 0, "Factory",
                       "Factory", "Factory"),
        TransportState("Car_2", MoveMethod.GROUND, -1, 0, 0, "Factory",
                       "Factory",
                       "Factory"),
        TransportState("Ship", MoveMethod.WATER, -1, 0, 0, "Port", "Port",
                       "Port"),
    ]

    for i in input_distance:
        routes.append(Route(i["B"], i["E"], i["D"], i["T"]))
        routes.append(Route(i["E"], i["B"], i["D"], i["T"]))

    id = 0
    for c in cargo_list:
        id += 1
        cargos.append(Cargo(id, "Factory", c, "Factory", ""))
        warehouses[0].cargoids.append(id)

    time = 0

    # print(warehouses_connected(routes,"WH_B","Port",MoveMethod.GROUND))
    while True:
        print("TIME {}".format(time))
        print("")

        for w in warehouses:
            if len(w.cargoids)>0:
                print("- {} cargos:{}".format(w.name,w.cargoids))

        # for t in transports:
        #     t.try_to_complete(time, warehouses, cargos)

        for t in transports:
            t.next_step(time, warehouses, cargos, routes)

        is_finished = True
        for c in cargos:
            if c.current_state != c.end:
                is_finished = False

        if is_finished:
            break
        if time>100:
            break

        time += 1
        print("")

    print("")
    print("Toatal time: {}".format(time))
