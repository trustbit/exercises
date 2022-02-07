[Back to index](transport-tycoon.md) 

# Episode 2.1 - Find shortest path on map

In the previous season of DDD katas we were working with a static route. Trucks and ferries were travelling along the predefined route.  

**Now it is the time to make things more realistic.** Transports normally aren't bound to a route and are free to find their own route on a map. Routing algorithm is the heart of any transport-based system, be it Transport Tycoon or Google ETA. 

![image-20220207105046047](images/image-20220207105046047.png)

**Task**: write a short code that can take names of two cities and print out the shortest path between them. For example: 

```
$ route Steamdrift Leverstorm
Steamdrift,Irondale,Rustport,Leverstorm
```

Here is the CSV [map with the distances](transport-tycoon/s02e01_map.csv).