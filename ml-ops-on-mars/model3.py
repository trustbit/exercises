#!/usr/bin/env python
import sys
import time
import json
import math



def model_predict(data):
    if 'data' not in data:
        raise ValueError("data should have 'data' field")
    data = data['data']

    print("Start calculations")
    started = time.time()

    # perform the computations
    time.sleep(abs(math.tan(data)))

    print("Done in {:.2f}sec".format(time.time() - started))
    # we have the result now
    result = {'ice_found': True}
    return result


def main():
    print("initializing model...")
    for i in range(5):
        time.sleep(1)
        print(f" {i}")
    print("ready: Model-initialized")


    print("Loading data from the stdin")

    for line in sys.stdin:
        if not line.strip():
            continue
        request = json.loads(line)
        print("input: " + json.dumps(request))
        result = model_predict(request)
        print("result: " + json.dumps(result))


if __name__ == "__main__":
    main()
