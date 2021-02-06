[⬅️ previous](exercise1.md) | [inbox](readme.md) | [next ➡️](exercise3.md)

# ML Ops 2: We lost one rover

Hi!

Your wrapper worked very well and allowed us to deploy the new model to production. Unfortunately we lost one of the rovers on the day one.

The model representation from the previous email missed one important nuance: computation time is non-deterministic. In some edge cases the model can take more than a few minutes to compute. This deadlocks the rover and could fry its motor control board (since the API integration was bolted on in a very crude way).

Could you, please, take a look at the [attached model](model2.py) representation? It would be great if your model wrapper would keep a track of execution time, terminating the model if it takes more than 10 seconds. Please just return something like `{ "error": "model timeout" }`


For example, to execute the model via the command-line, you can:

```
director@mex25pl ice-seeker (api-experiment)> echo "{\"data\":1}" | python model2.py
Loading data from the stdin
input: {"data": 1}
Start calculations
Done in 1.56sec
result: {"ice_found": true}
```

If you send `{"data":33}` that would trigger a very lengthy computation that should be aborted by the API after 10 seconds.

We are counting on you!

Best regards,  
Colony Director

<img src="https://www.nasa.gov/sites/default/files/thumbnails/image/pia23378-16.jpg">

## Task

Please protect the Rovers from the misbehaving models!

You need to update your model wrapper API (from the [first exercise](exercise1.md)) so that it
would abort the HTTP call in case the model takes more than 10 seconds to execute.

## Solutions

Please feel free to send PRs that add your solution to this list. 

- [ajukraine](https://github.com/ajukraine): [F#](https://github.com/ajukraine/ml-ops/tree/exercise-2)
- [saintedlama](http://github.com/saintedlama): [node.js](https://github.com/saintedlama/ml-ops-on-mars/tree/exercise-2)
- [pfournea](https://github.com/pfournea): [Kotlin](https://github.com/pfournea/ml_ops_on_mars/blob/exercise2/src/main/kotlin/be/pfournea/mlopsonmars/exercise1/controller/PythonProxyController.kt)
- [Your Name](http://github.com/your-github-profile): [programming language](http://github.com/url-to-the-ml-ops-solution-2)
- 


## Next

[✉️ 1 unread message](exercise3.md)

