from flask import Blueprint, request, jsonify
from app.services.ai_service import get_ai_response
import json

prediction_bp = Blueprint("prediction", __name__)

@prediction_bp.route("/predict", methods=["POST"])
def predict():

    # Get JSON data from Postman
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"})

    # Get symptoms from JSON
    symptoms = data.get("symptoms")

    # Check if symptoms are provided
    if not symptoms:
        return jsonify({"error": "Please enter symptoms"}), 400

    # Send symptoms to AI
    response = get_ai_response(symptoms)

    # Convert AI JSON string into Python dictionary
    response = json.loads(response)

    # Return JSON response
    return jsonify(response)