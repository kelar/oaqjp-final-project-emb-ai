"""
Flask web server for Emotion Detection application.

This module defines the Flask web server and its endpoints for the Emotion Detection application.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template for the root route.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    """
    Handle the emotion detection endpoint.
    
    This function handles GET requests 
    and retrieves the text to be analyzed from the query parameters.
    It returns the emotion scores and the dominant emotion as a JSON response.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is not None:
        result = emotion_detector(text_to_analyze)
        if result['dominant_emotion'] is None:
            response = {"error": "Invalid text! Please try again!"}
            return jsonify(response)
        response = {
            "anger": result['anger'],
            "disgust": result['disgust'],
            "fear": result['fear'],
            "joy": result['joy'],
            "sadness": result['sadness'],
            "dominant_emotion": result['dominant_emotion']
        }
        return jsonify(response)
    return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
