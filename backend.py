from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Placeholder news data
news_data = [
    {"title": "New Infrastructure Projects Announced", "category": "Politics", "sentiment": "positive"},
    {"title": "Severe Weather Warning Issued", "category": "Weather", "sentiment": "negative"},
    {"title": "Tourism Industry Reports Record Growth", "category": "Economy", "sentiment": "positive"},
]

alerts = [
    {"message": "Heavy rain expected in Malé", "type": "weather", "priority": "high"},
    {"message": "Major accident on main highway", "type": "emergency", "priority": "critical"}
]

@app.route('/news', methods=['GET'])
def get_news():
    return jsonify(news_data)

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts)

@app.route('/trends', methods=['GET'])
def get_trends():
    trends = {"Politics": random.randint(5, 20), "Economy": random.randint(10, 30), 
              "Weather": random.randint(3, 15), "Health": random.randint(5, 25)}
    return jsonify(trends)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from Render, fallback to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
