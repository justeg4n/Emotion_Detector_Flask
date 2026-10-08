import requests
import json

def emotion_detector(text_to_analyse):
    empty_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    # Blank input: nothing to analyse
    if not text_to_analyse or not text_to_analyse.strip():
        return empty_result

    # Watson NLP emotion-prediction endpoint (IBM Skills Network lab environment)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    try:
        response = requests.post(url, json=input_json, headers=header, timeout=10)
    except requests.exceptions.RequestException:
        # Service unreachable (e.g. outside the lab network)
        return empty_result

    # Invalid input is reported by the service with status 400
    if response.status_code == 400:
        return empty_result

    formatted_response = json.loads(response.text)

    # Extract required emotions
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']

    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }