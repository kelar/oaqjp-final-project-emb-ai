import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    response_dict = response.json()

    # Debugging print statement to check the response
    print("Response JSON:", response_dict)

    # Extracting emotion scores correctly from the response JSON
    if 'emotionPredictions' in response_dict and len(response_dict['emotionPredictions']) > 0:
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
    else:
        emotion_scores = {'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0}

    # Debugging print statement to check the extracted emotion scores
    print("Emotion Scores:", emotion_scores)

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores


