# edge-anomaly-detection

Build Config and Image Stream

```
oc apply -f serve.bc.yaml
```

Seldon Deployment

```
oc apply -f serve.selcon.yaml
```

You can change `MODEL_THRESHOLD` env var to modify the threshold for anomaly

## Example query

Passing in a number **5**

```
curl -k -X POST -H 'Content-Type: application/json' -d "{'data': {'ndarray': [5]}}" https://$(oc get route anomaly-detection -o jsonpath='{.spec.host}')/api/v0.1/predictions
```

Response

```
{
  "meta": {
    "puid": "5qkdur66pmtagbcetf75b5qdat",
    "tags": {
    },
    "routing": {
    },
    "requestPath": {
      "anomaly-detection": "anomaly-detection-serve"
    },
    "metrics": []
  },
  "data": {
    "names": [],
    "ndarray": [0.0]
  }
}
```

Notice `ndarray: [0.0]` - that means `False` - i.e. **not** an anomaly

Passing in a number **50**

```
curl -k -X POST -H 'Content-Type: application/json' -d "{'data': {'ndarray': [50]}}" https://$(oc get route anomaly-detection -o jsonpath='{.spec.host}')/api/v0.1/predictions
```

Response

```
{
  "meta": {
    "puid": "f05tvk4g8shrq84gkmruf4gicd",
    "tags": {
    },
    "routing": {
    },
    "requestPath": {
      "anomaly-detection": "anomaly-detection-serve"
    },
    "metrics": []
  },
  "data": {
    "names": [],
    "ndarray": [1.0]
  }
}
```

Notice `ndarray: [1.0]` - that means `True` - i.e. it *is* an anomaly