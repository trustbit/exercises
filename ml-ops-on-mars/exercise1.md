# ML Ops 1: I heard that you know programming...

Hi!

Our scientists found a way to improve search algorithms of the Ice-seeker
Martian Rovers. It should help us to reach sustainability a couple of months earlier!
There is one catch - new algorithm requires special hardware and could run only
on our mainframe. So we need to setup an API through which the Rovers could
submit Martian soil scans to the ML model and get the results back.

I heard that you know programming. Could you take a stab in
implementing that API wrapper for us?

The model could be represented by this Python script (we'll just plug the model
later where `thread.sleep` currently is). It reads a request from the stdin,
runs the computations and writes result back to the stdout. The output might contain
different text, but the result is always a JSON object on a single line, prefixed by `result: `.


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

Best regards, 
Colony Director

<img src="https://photojournal.jpl.nasa.gov/jpegMod/PIA17944_modest.jpg">

## Task

Please make the Data Scientists of Mars happy!

You can use the language of your choice to implement the API that forwards incoming requests to the Python model. Naturally, the API should respond with whatever JSON result the model returns.

Should you have any questions, don't hesitate to ask them in the [MLOps Community Slack](https://go.mlops.community/slack). You could mention `@abdullin` to get a faster response.

Once done, please check out the [exercise2.md](next message).

## Solutions

Please feel free to send PRs that add your solution to this list. 

- [saintedlama](http://github.com/saintedlama): [node.js](https://github.com/saintedlama/ml-ops-on-mars/tree/exercise-1)
- [marketzer](https://github.com/marketzer): [Python](https://github.com/marketzer/ml-ops-on-mars)
- [ajukraine](https://github.com/ajukraine): [F#](https://github.com/ajukraine/ml-ops)
- [Your Name](http://github.com/your-github-profile): [programming language](http://github.com/url-to-the-ml-ops-solution-1)
- 


