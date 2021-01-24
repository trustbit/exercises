#!/usr/bin/env python
import sys
import time
import json
import math


TPU_COUNT = 1


import filelock as lock
def acquire_tpu():

    # cycle throughout the TPUs until
    # one is available
    print("Scheduling a work on a TPU...")
    while True:
        for i in range(0, TPU_COUNT):
            try:
                l = lock.FileLock(f"{i}.lock", timeout=0.5)
                l.acquire()
                # we want to reuse the lock in with statement
                # without releasing it right now
                l._lock_counter -= 1

                print(f"Acquired TPU {i}")

                return l
            except lock.Timeout:
                continue

def model_predict(data):
    # run dedicated hardware

    with acquire_tpu():
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
