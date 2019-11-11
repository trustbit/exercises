module Exercise1

open System.Collections.Generic

type Cargo = A | B
type Truck = T1 | T2
type Timepoint = int

type Event =
    | CargoReadyForDelivery of Cargo
    | ArrivedBackAtFactory of Truck
    | ArrivedOnPort
    | ParkedShipmentAtPort
    | PickedUpShipmentAtPort
    | DeliveredShipment of Cargo

type Entry = Event * Timepoint

type State =
    { mutable TrucksAtFactory: Map<Timepoint, Queue<Truck>>
      mutable ShipWaitingAtPort: Timepoint
      CargoAtFactory: Queue<Cargo>
      mutable CargoWaitingForPickupAtPort: int
      mutable CurrentTime: Timepoint
      CargoDelivered: List<Cargo * Timepoint> }
      
let update (state: State) event =
    match event with
    | CargoReadyForDelivery c, _ -> state.CargoAtFactory.Enqueue c
    | ArrivedBackAtFactory t, time when state.TrucksAtFactory.ContainsKey time -> state.TrucksAtFactory.[time].Enqueue t
    | ArrivedBackAtFactory t, time -> state.TrucksAtFactory <- state.TrucksAtFactory.Add(time, Queue [ t ])
    | ArrivedOnPort, time -> state.ShipWaitingAtPort <- time
    | ParkedShipmentAtPort, _ -> state.CargoWaitingForPickupAtPort <- state.CargoWaitingForPickupAtPort + 1
    | DeliveredShipment c, time -> state.CargoDelivered.Add(c, time)
    | PickedUpShipmentAtPort, _ -> state.CargoWaitingForPickupAtPort <- state.CargoWaitingForPickupAtPort - 1

let moveCargoFromFactory state =
    state.TrucksAtFactory
    |> Map.tryFind state.CurrentTime
    |> Option.map (fun trucks ->
        Seq.init (System.Math.Min(state.CargoAtFactory.Count, trucks.Count)) (fun _ -> (state.CargoAtFactory.Dequeue(), trucks.Dequeue()))
        |> Seq.collect(fun (c, truck) -> 
            match c with
            | A ->
                [ Entry(ParkedShipmentAtPort, state.CurrentTime + 1)
                  Entry(ArrivedBackAtFactory truck, state.CurrentTime + 2) ]
            | B ->
                [ Entry(DeliveredShipment B, state.CurrentTime + 5)
                  Entry(ArrivedBackAtFactory truck, state.CurrentTime + 10) ]
            )
    )
    |> Option.toList
    |> Seq.collect id

let moveCargoFromPort state =
    if state.ShipWaitingAtPort <= state.CurrentTime && state.CargoWaitingForPickupAtPort > 0 then   
        [ Entry(PickedUpShipmentAtPort, state.CurrentTime)
          Entry(DeliveredShipment A, state.CurrentTime + 4)
          Entry(ArrivedOnPort, state.CurrentTime + 8) ]
    else []

let step state =
    moveCargoFromPort state
    |> Seq.iter (update state)

    moveCargoFromFactory state
    |> Seq.iter (update state)

let iterate (state: State) =
    while state.CargoAtFactory.Count > 0 || state.CargoWaitingForPickupAtPort > 0 do
        step state
        state.CurrentTime <- state.CurrentTime + 1

let findLatestDelivery (state: State) = state.CargoDelivered |> Seq.maxBy (fun (_, t) -> t)

let parseInput (input: string []) =
    match input with
    | [| singleArgument |] ->
        singleArgument.ToCharArray()
        |> Seq.map (function
            | 'A' -> A
            | 'B' -> B
            | x -> failwithf "Unknown cargo %c" x)
    | x -> failwithf "Expecting a single string containing the cargo list but got %A" x

[<EntryPoint>]
let main argv =
    printfn "%A" argv
    let cargo = 
        parseInput argv
        |> Seq.toList
        |> List.map(fun c -> CargoReadyForDelivery c, 0)

    let initialTrucks = 
        [ 
            ArrivedBackAtFactory T1,0
            ArrivedBackAtFactory T2 ,0
        ]

    let state =
        { TrucksAtFactory = Map.empty
          CargoAtFactory = Queue()
          CargoDelivered = List() 
          CurrentTime = 0          
          ShipWaitingAtPort = 0
          CargoWaitingForPickupAtPort = 0
          }

    Seq.concat [cargo ; initialTrucks]
    |> Seq.iter (update state)    

    iterate state
    let highest = findLatestDelivery state
    printfn "Highest time %A" highest

    0 // return an integer exit code
