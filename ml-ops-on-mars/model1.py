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
