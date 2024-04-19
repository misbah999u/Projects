# End-to-end Fake News Classifier


## Building UI

```cd webapp && npm run build```

## Running service (+ Serving UI)

```gunicorn -t 120 -b :8080 app:app```

Will run the app on http://localhost:8080