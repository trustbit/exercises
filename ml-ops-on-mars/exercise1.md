# ML Ops on Mars: Exercise 1

> I heard that you know programming...

Hi!

Our scientists found a way to improve search algorithms of the Ice-seeker
Rovers. It should help us to reach sustainability a couple of months earlier!
There is one catch - new algorithm requires special hardware and could run only
on our mainframe. So we need to setup an API through which the Rovers could
submit Martian soil scans to the ML model and get the results back.

I heard that you know your way around the computers. Could you take a stab in
implementing that API wrapper for us?

The model could be represented by this Python script (we'll just plug the model
later where `thread.sleep` currently is). It reads a request from the stdin,
runs the computations and writes result back to the stdout (always as a JSON
object on a single line, prefixed by `result: `).


```python
#!/usr/bin/env python
import sys
import time
import json

def model_predict(data):
    # run dedicated hardware
    print("Start calculations")
    time.sleep(2)
    print("Done")
    # we have the result now
    result = { 'ice_found': True }
    return result

def main():
    print("Loading data from the stdin")

    request = json.load(sys.stdin)

    print("input: " + json.dumps(request))
    result = model_predict(request)
    print("result: " + json.dumps(result))

if __name__ == "__main__":
    main()

```

For example, to execute the model via the command-line, you can:

```
> echo "[1,2,42]" | python model1.py
Loading data from the stdin
input: [1, 2, 42]
Start calculations
Done
result: {"ice_found": true}
```

Data scientists would like to have an HTTP API that handles JSON requests on
`http://localhost:8080/predict` by proxying them to the Python model. You can
keep the model source code in the same folder with the HTTP API server.

I understand that this is not exactly what you came to Mars for, unfortunately
you are all we've got. The Colony depends on you.

Best regards, Colony Director
