#!/usr/bin/env python
import sys
import time
import json
import math

def model_predict(data):
    # run dedicated hardware
    print("Start calculations")
    started = time.time()

    if 'data' not in data:
        raise ValueError("data should have 'data' field")
    data = data['data']
    # perform the computations
    time.sleep(abs(math.tan(data)))

    print("Done in {:.2f}sec".format(time.time() - started))
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
