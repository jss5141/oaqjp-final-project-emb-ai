"""
Flask web server for the Emotion Detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page for user interaction.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Handles emotion detection request.

    Returns:
        str: Formatted response if text is provided, otherwise an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
