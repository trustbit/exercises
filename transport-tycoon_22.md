Previous: [Find shortest path on map](transport-tycoon_21.md) | [Index](transport-tycoon.md) 

# Episode 2.2: Compute ETA with fixed speed

Before we go to data mining, let's handle one more step. Let's compute Estimated Time of Arrival (ETA) between any two locations on the map.

This task is similar to the previous kata. The difference is:

- previously we computed the **shortest path** between two locations
- now we need to compute **fastest path** between any two locations

We know distances between the cities. To get the travel time we also need to know the speed.

For this exercise we'll assume that the speed is constant and fixed per road.

Here is the CSV [map with the road speed](transport-tycoon/s02e02_map.csv). Or in plain text:

```
A               B               km    speed
Cogburg         Copperhold      1047     91
Leverstorm      Irondale        629      89
Cogburg         Steamdrift      1269     89
Copperhold      Irondale        345      91
Copperhold      Leverstorm      569      91
Leverstorm      Gizbourne       866      91
Rustport        Cogburg         1421     93
Rustport        Steamdrift      1947     99
Rustport        Gizbourne       1220     96
Irondale        Gizbourne       526      97
Cogburg         Irondale        1034     98
Rustport        Irondale        1302     95
```



## Task

Write a console applocation that takes names of two cities, computes the fastest route and prints out the milestones between them. For example:

```bash
> route Steamdrift Leverstorm
```

and the output:

```
 0.00h  DEPART  Steamdrift
14.26h  ARRIVE  Cogburg
24.81h  ARRIVE  Irondale
31.88h  ARRIVE  Leverstorm
```

Remember, that *the map is not the terrain*. The shortest path isn't always the fastest.

It is assumed that the input is valid. There is no need to check it for correctness.

## Implementation Notes

One way to implement the solution is to take the shortest-path algorithm and use the route to compute the milestones. This will lead to the suboptimal route.

Another way is to use the shortest-path algorithm, but instead of the road distance use road travel time. We can compute it by `road.km/road.speed`.

## Next

- Contribute your solution to [a list of all solutions](transport-tycoon/README.md)! Linked page explains how to do that.
- If you have any questions or comments - we have a [Discord chat](https://discord.gg/jHGbUwxDgv).
- Next episode will be published within 2 weeks. You can watch this repository or [subscribe to the mailing list](https://tinyletter.com/softwarepark).
- 🔜 Episode 2.3: Mine historical data for travel speed