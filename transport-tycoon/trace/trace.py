#!/usr/bin/python
"""
Utility converts log output from the transport tycoon exercise #2 into
the chrome trace viewer format
"""


import sys
import os
import json

if len(sys.argv) == 1:
    print("Must pass a log file to parse")
    sys.exit(1)

events = []


def extract_common_headers(e):
    name = "{0}:{1}".format(e['kind'], e['transport_id'])

    cargo = ["CARGO:{0}_{1}_{2}".format(x['origin'], x['destination'], x['cargo_id']) for x in e.get('cargo', [])]

    return {
        'ts': e['time'],
        'pid': name,
        'tid': name,
        'cat': 'ddd',
        'args': {'cargo': cargo, 'transport': name},

    }


input_file = sys.argv[1]




with open(input_file, 'rt') as log:
    for l in log:
        if not l or l.startswith('#'):
            continue

        e = json.loads(l)
        kind = e['event']
        if kind == 'DEPART':
            headers = extract_common_headers(e)
            headers.update({'ph': 'B', 'name': "{0}-{1}".format(e['location'], e['destination']), })
            events.append(headers)

        if kind == 'ARRIVE':
            headers = extract_common_headers(e)
            headers.update({ 'ph': 'E'})

            events.append(headers)
        if kind == 'LOAD' or kind == 'UNLOAD':
            if not e['duration']:
                continue

            headers = extract_common_headers(e)
            headers.update({'ph': 'X', 'dur':e['duration'], 'name':kind})
            events.append(headers)




    print(json.dumps({"displayTimeUnit": "ms", 'traceEvents': events, }, indent=True))
