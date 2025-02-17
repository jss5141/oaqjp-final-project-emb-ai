import requests
import json  # Import json for response parsing

def emotion_detector(text_to_analyze):
    """
    This function sends a request to Watson NLP's Emotion Detection API,
    extracts relevant emotions (anger, disgust, fear, joy, sadness),
    and determines the dominant emotion. Handles errors for invalid input.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=headers)  # Send POST request
    
    # Handle error cases
    if response.status_code == 400:  # Invalid text input case
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)  # Convert response text to dictionary

    # Extract emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get) if emotions else None

    # Return formatted output
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
