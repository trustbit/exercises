Previous: [Compute ETA with fixed speed](transport-tycoon_22.md) | [Index](transport-tycoon.md) 

# Episode 2.3: Mine historical data for travel speed

In the previous exercise we computed Estimated Time of Arrival (ETA) for a cargo truck. 

The truck moved between two locations with a **predefined speed**. We wrote a script that loaded predefined travel speed for each road from the files and computed fastest travel route between any two locations:

```bash
> route Steamdrift Leverstorm
 0.00h  DEPART  Steamdrift
14.26h  ARRIVE  Cogburg
24.81h  ARRIVE  Irondale
31.88h  ARRIVE  Leverstorm
```

In the real world we would not have predefined travel times provided for us. We would need to **mine historical data** in order to figure out the travel speed between locations. 

Historical data can be mined for the insights and used to **train models**. The trained model could then be used to *predict* things that didn't happen yet. 

Also, in the real world we would need to **validate the quality of our model**. 

We can do that by "hiding" some observations from the model and trying to predict the outcome. Then we compare observed outcome with the predicted one. Smaller is the difference - more accurate is the model.

Let's focus on minimalistic training and validation in this exercise.

## Training

We have a training dataset [s02e03_train.csv](transport-tycoon/s02e03_train.csv). It is a CSV file with the travel history. It looks similar to the output from the previous exercise:

![image-20220310150706585](images//image-20220310150706585.png)

This file is a travel log of a company that runs multiple trucks. Whenever there is a delivery from A to B:

- New row is added with a unique `transport_id`, timestamp, starting location and `DEPART` event
- One row is added for each intermediate and final milestone with `ARRIVE` event.

We can mine that file for a history of travel times between two locations: 

- load each trip from the file (uniquely identified by value in `TRANSPORT` column);
- each trip will have one or more segments, represented by `DEPART` event and one or more `ARRIVE` events;
- for each road segment we can compute observed travel time by substracting arrival time from the departure: `travel_time = arrival_time - departure_time`.

For example:

```
# CARGO-999
DEPART Leverstorm at December 03, 16:00
ARRIVE Irondale at December 03, 23:03
ARRIVE Rustport at December 04, 12:07
```

From this we can infer that:

- `Leverstorm` to `Irondale` took 23:03 - 16:00 = 07:03 hours
- `Irondale` to `Rustport` happened overnight from December 03 23:03 to Dec 04 12:07. It took 13:04 minutes (time difference between these timestamps)

By repeating that process for each transport, we will gather multiple slightly different travel times (or samples) for each road segment.

We can compute an average over these times to compute road travel time that we can plug into the model:`travel_time = sum(travel_time_samples) / len(travel_time_samples)`

Repeat that for each road, then load the numbers into the model from the previous exercises, and you could *predict* travel time between any two locations. 

To reiterate:

1. Load travel history from [s02e03_train.csv](transport-tycoon/s02e03_train.csv).
2. Convert timestamps into travel duration times for each road.
3. For each road compute an average travel time. 
4. Load this data into the model from the previous exercise.

The model is now trained to predict travel times using insights from the travel history.

## Validation

How do we validate our findings? How do we know if our predictions make any sense?

There is a separate dataset that we could use to validate our results: [s02e03_test.csv](transport-tycoon/s02e03_test.csv). 

This CSV files contains real (or *oserved*) travel times (in hours) between two locations (ATA stands for `Actual Time of Arrival`).

![image-20220310150638459](images/image-20220310150638459.png) 

We could validate our model by going through each row in this validation dataset and computing the travel time that our model would predict. Then we compare results with the `ATA` column from this table.

```
PREDICTED TRAVEL TIME | ACTUAL TRAVEL TIME | ERROR      | NOTE
16:23:01              | 16:24:59           | ~2 minutes | This is quite good!
20:44:12              | 12:42:22           | ~8 hours   | The model is WAY off here
```

Smaller the difference between these numbers (or *error*)- more accurate the model is.

In order to communicate model accuracy to the others, we would need to somehow **aggregate all errors into a single model error**. 

Averaging over errors wouldn't work here. Imagine you have two travel results:

```
PREDICTED TRAVEL TIME | ACTUAL TRAVEL TIME | ERROR      |
1 hour                | 2 hours            | 1 hour     |
2 hours               | 1 hour             | -1 hour    |
```

If we average these two errors we would get `0` - which is the perfect score. 

Let's use *Mean Squared Error* (MSE) instead. It is good enough for this exercise.

![e258221518869aa1c6561bb75b99476c4734108e](images/e258221518869aa1c6561bb75b99476c4734108e.svg)

The equation might look scary because of the notation. it simply means:

1. Compute *error* by substracting observed value from the predicted.
2. Compute a square of each error
3. Compute *mean* (also known as *average*) of these squared errors. 

In pseudocode this could look like:

```python
error_sum = 0
for loc_a, loc_b, actual_hours in test_dataset:
  preducted_hours = predict(loc_a, loc_b)
  difference = actual_hours - predicted_hours
  square = difference * difference
  error_sum += square
mse = error_sum / len(test_dataset)
print(f"Mean squared error is {mse}")
```

To reiterate:

1. For each row in [s02e03_test.csv](transport-tycoon/s02e03_test.csv) use the trained model to predict travel time.
2. For each row compute error by computing difference between the observed travel time (from the file) and predicted travel time (from the model).
3. Aggregate these errors into a single error number by using Mean Squared Error formula.

## Task

Write a console application that:

- uses training dataset `s02e03_train.csv` to compute average travel times for each road;
- predicts travel times in hours for each row in validation dataset  `s02e03_test.csv`;
- computes Mean Squared Error for these predictions and prints the result.

For example:

```
> python3 solution_s0203.py
MSE is 0.37877778702
```

The number above is just a sample. Your number will be slightly different :)

## Next

- Contribute your solution to [a list of all solutions](transport-tycoon/README.md)! Linked page explains how to do that.
- If you have any questions or comments - we have a [Discord chat](https://discord.gg/jHGbUwxDgv).
- Next episode will be published within 2 weeks. You can watch this repository or [subscribe to the mailing list](https://tinyletter.com/softwarepark).
- 🔜 Episode 2.4: Setup training pipeline and iterate

