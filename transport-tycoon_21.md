[Index](transport-tycoon.md) | Next: [Compute ETA with fixed speed](transport-tycoon_22.md)

# Episode 2.1 - Find shortest path on map

In the previous season of DDD katas we were working with a static route. Trucks and ferries were travelling along the predefined route.  

**Now it is the time to make things more realistic.** Transports normally aren't bound to a route and are free to find their own route on a map. Routing algorithm is the heart of any transport-based system, be it Transport Tycoon or Google ETA. 

Take a look at this map (exact distances are provided below). How can a truck find the shortest route between any two locations? 

![image-20220207105046047](images/image-20220207105046047.png)



## Task

Write a short code that can take names of two cities and print out the shortest path between them. For example: 

```
$ route Steamdrift Leverstorm
Steamdrift,Irondale,Rustport,Leverstorm
```

Here is the CSV [map with the distances](transport-tycoon/s02e01_map.csv). Or in plain text:

```
A           	B           	km
Cogburg     	Copperhold  	1047
Leverstorm  	Irondale    	673
Cogburg     	Steamdrift  	1269
Copperhold  	Irondale    	345
Copperhold  	Leverstorm  	569
Leverstorm  	Gizbourne   	866
Rustport    	Cogburg     	1421
Rustport    	Steamdrift  	1947
Rustport    	Gizbourne   	1220
Irondale    	Gizbourne   	526
Cogburg     	Irondale    	1034
Rustport    	Irondale    	1302
```

## Implementation Notes

One possible implementation is to use [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm):

![Dijkstra_Animation](images/Dijkstra_Animation.gif)

1. Mark all locations as *unvisited*. Create a list of all unvisited locations called the *unvisited set*.
2. Assign to every location a *tentative distance* value: set it to zero for our initial location and to infinity for all other locations. This is the shortest path to that location discovered so far. Set the starting location as current.
3. For the current location, consider all of its unvisited neighbors and calculate their tentative distances through the current location. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current location *A* is marked with a distance of 6, and the road connecting it with a neighbor *B* has length 2, then the distance to *B* through *A* will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
4. When we are done considering all of the unvisited neighbors of the current location, mark the current one as visited and remove it from the unvisited set. A visited location will never be checked again.
5. If the destination location has been marked visited (when planning a route between two specific location) or if the smallest tentative distance among the location in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial location and remaining unvisited locations), then stop. **The algorithm has finished.**
6. Otherwise, select the unvisited location that is marked with the smallest tentative distance, set it as the new *current location*, and go back to step 3.

## Next

- Contribute your solution to [a list of all solutions](transport-tycoon/README.md)! Linked page explains how to do that.
- If you have any questions or comments - we have a [Discord chat](https://discord.gg/jHGbUwxDgv).
- Next episode will be published within 2 weeks. You can watch this repository or [subscribe to the mailing list](https://tinyletter.com/softwarepark).
- Episode 2.2: [Compute ETA with fixed speed](transport-tycoon_22.md)