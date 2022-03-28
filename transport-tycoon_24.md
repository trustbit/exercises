# Episode 2.4: Connect speed model to the simulation

In previous exercises we have done two things:

- Created a code to find a fastest route between any two locations (Started in 2.1 and finished in 2.2). This model used predefined travel speeds.
- Created a model to mine historical data and estimate speed for each road (Done in 2.3).

Now it is the time to plug these two together in a iterative loop.

> This is a kind of work that ML Operations Engineer would be doing in a team.



## Task

Write an application that runs these two steps in one iteration. It could also be a couple of separate applications that run in a sequence.

Given the input file:

```bash
> train_model s02e04.csv
MSE is 4444.44
Saved to speeds.csv

> run_simulation map.csv speeds.csv 

```







