# trace.py

This is a utility that takes domain event log format from the transport tycoon log and converts into the Chrome Trace Viewer format. 

**You need to have python installed on your system.**

For example to, convert the domain log from file `AB.log` and print to the screen:

```bash
$ python trace.py AB.log
```

Or to write to the file, you just pipe the outputs there:

```bash
$ python trace.py AB.log > AB.trace
```

Once you have the trace file. You can launch Google Chrome and navigate to the `chrome://tracing` url. 

Then to load the file:

* click on the `Load` button

* drag-and-drop the trace file.
