# Emotion Detector (Python / Flask)

A Flask web application that detects emotions in English text using the **Watson NLP** emotion-prediction service. Users type a sentence in the browser and get scores for anger, disgust, fear, joy and sadness, plus the dominant emotion. Based on the IBM Skills Network `oaqjp-final-project-emb-ai` template (Apache-2.0).

## Features

- `EmotionDetection` Python package wrapping the Watson NLP REST endpoint
- Returns the five emotion scores and the dominant emotion
- Handles blank input, HTTP 400 responses and an unreachable service by returning empty results
- Flask server with a simple HTML / JavaScript front end (AJAX call to `/emotionDetector`)
- Unit tests for each dominant emotion

## Run

```bash
pip install -r requirements.txt
python server.py                         # http://localhost:5000
python -m unittest test_emotion_detection.py
```

> The Watson NLP endpoint is only reachable from the IBM Skills Network lab environment. Outside it, the app responds "Invalid text! Please try again!" and the unit tests fail because no predictions are returned.

## Project structure

```
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py   # Watson NLP client
├── server.py                  # Flask routes
├── templates/index.html       # UI
├── static/mywebscript.js      # AJAX request to the API
└── test_emotion_detection.py  # unit tests
```

---
Author: Nguyen Quoc Anh — FPT University
