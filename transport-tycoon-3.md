 [Back to index](transport-tycoon.md) | [Exercise 2](transport-tycoon-2.md)

# Exercise 3

Let us take a moment and review what we already have:

- understanding of the simplified Transport Tycoon domain;

- an implementation that captures core behaviors;

- mechanism which logs important events in the text form;

- a trace.py tool that could be used to visualise and troubleshoot problematic workflows.

*How does this even relate to the Domain-Driven Design?*

First of all, **our event logging is a simple form of publishing domain events**. We capture important state transitions in a predefined format. It is done in such a form that:

- downstream teams or domains could consume these events independently  from the publishing code or its language. For example, trace.py is written in Python, while most of the DDD solutions are in C#.

- changes in the domain behavior may enrich, but don't break existing event log format; we've observed that while introducing complexity to the SHIP.

There is also another visualization implementation that builds up on the domain events. It is done by [Aigiz Kunafin](https://github.com/AigizK/) in [HTML+JS](https://github.com/AigizK/transport-tycoon/blob/master/transport_visulazation/index.html). 

Second, **the domain language found its way into each and every codebase**, even though we didn't mention any coding patterns. Regardless, of the implementation language, exercise solutions would make sense to anybody familiar with the domain. 

Take a list at a few snippets from the [list of solutions](https://github.com/Softwarepark/exercises/blob/master/transport-tycoon/README.md).

[F#](https://github.com/Nagelfar/ddd-exercises/blob/master/exercise2/Exercise2.fs#L106-L111) by Christian Folie:

```fsharp
let pickUpCargoAtFactory time cargos vehicles =
 let potentialTruck = findVehicleType findTruck vehicles
 match cargos |> List.tryHead, potentialTruck with
 | Some((_, A) as c), Some truck -> transportLeg time [ c ] (Truck truck) Factory Port
 | Some((_, B) as c), Some truck -> transportLeg time [ c ] (Truck truck) Factory (Warehouse B)
 | _ -> []
```

[PHP](https://github.com/gquemener/TransportTycoon/blob/master/src/TransportTycoon/Domain/Model/Operation/LoadCargoInAvailableVehicle.php#L22-L29) by Gildas Quéméner:

```php
foreach ($cargos as $cargo) {
    if ($cargo->isStoredInFacility($vehicle->position())) {
        $load[] = $cargo;
    }
    if (count($load) === $vehicle->maxLoad()) {
        break;
    }
}
```

[C#](https://github.com/jkonecki/SoftwarePark/blob/master/TransportTycoon/TransportTycoon/Vehicle.cs#L63-L74) by Jakub Konecki:

```csharp
public void Unload()
{
    if (this.Action != Action.Unloading)
        return;

    this.Location.UnloadContainer(this.Container);
    this.Container = null;

    this.Action = Action.Returning;
    this.TravellingEta = this.Route.Length;
    this.Location = null;
}
```

[Go](https://github.com/danielmahadi/transport-tycoon-go/blob/exercises/1/main.go#L99-L108) by Daniel Mahadi:

```go
plan := Plan {
    Vehicle: t.Vehicle,
    Location: t.Location,
    Cargo: t.Cargo,
}

if route, isInMap := MAP[plan]; isInMap {
    t.Location = route.Location
    t.Eta = route.Duration + TIME
}
```

[Kotlin](https://github.com/pfournea/transport-tycoon/blob/master/src/main/kotlin/be/transporttycoon/transporttycoon/TransportService.kt#L13-L26) by Peter Fourneau:

```kotlin
trucks.forEach { truck ->
    if (truck.atFactory()) {
        val transportAvailableForTruck = findTransportForTruck(transportList)
        transportAvailableForTruck?.let { truck.loadTransport(it) }
    }
    if (truck.atDestination()) {
        if (truck.transport!!.destination == Destination.A) {
            port.transportList.add(truck.transport!!)
        }
        truck.unload()
    }

    truck.move()
}
```

[TypeScript](https://github.com/mrothNET/transport-tycoon-exercises/blob/master/exercise2/src/routing.ts#L4-L12) by Michael Roth:

```typescript
const routingTable: { [origin: string]: { [destination: string]: TourPlaner } } = {
  FACTORY: {
    PORT: new TourPlaner(1),
    B: new TourPlaner(5),
  },
  PORT: {
    A: new TourPlaner(1, 6, 1),
  },
};
```

and [Clojure](https://github.com/yanisurbis/transport-tycoon/blob/master/src/transport_tycoon/core.clj#L103-L110) by Yanis Urbis:

```clojure
(defn get-next-ship-action-type [system ship]
  (let [payload (get-element-from-queue system :port)
        actor-position (:position ship)]
       (case [payload actor-position]
          [:a :a] :a->port
          [nil :a] :a->port
          [:a :port] :port->a
          :wait)))
```

Each of these snippets have ingrained aspects of the underlying domain into the codebase. That is one of the basic ways of handling domain complexity from within the codebase.

Third, **we have a form of event-driven specifications for our domain**. Each specification could be represented by:

- **WHEN scenario** (e.g. when scenario "AB")

- **THEN EXPECT events** (e.g. truck1 loads A and departs to port, truck2 loads B and departs to the B etc)

If you think of it, our **domain implementation could be considered valid as long as for each scenario it emits the same event logs**. In other words, *the event logs specify the exepected behavior for each scenario*.

We could test the validity of the implementation by running different scenarios and comparing resulting events with a well-known standard.

This gives us the opportunity to evolve the domain, get rid of the technical debt or explore new approaches.

In fact, let us do exactly that. Lets practice a little bit of TDD/BDD and **rewrite our solution in a completely different language**. Event logs generated by the second exercise will be our "gold standard".

## Task

- **Review existing solutions** from the solution list, identify things that you like and could build upon.

- **Pick any language that is different** from your original implementation. Perhaps, even pick the language that will improve the implementation somehow?

- **Reimplement your solution in that language**, making sure that it generates the same event logs as your previous solution.

## Exercise Notes

- Don't try to port your code exactly to another language. Try rewriting the solution from scratch. Some idioms are expressed in different languages differently. 

- Don't be afraid to do bold refactorings or changes. There is a safety net in the form of scenarios.

- **Build and improve upon the solutions of others!**

- Don't hesitate to ask people about their implementations (by creating an issue on their repository or asking a question in the [github discussions](https://github.com/orgs/ddd-exercises/teams/tt/discussions)).

## The END

This is currently the end of the Transport Tycoon exercises. You can check out the other exercise sets or subscribe to the [newsletter for the updates](https://tinyletter.com/softwarepark).
