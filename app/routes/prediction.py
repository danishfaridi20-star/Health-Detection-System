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

    # Get disease from JSON
    disease = data.get("disease")

    # Check if disease are provided
    if not disease:
        return jsonify({"error": "Please enter disease"})

    # Send disease to AI
    response = get_ai_response(disease)

    # Convert AI JSON string into Python dictionary
    response = json.loads(response)

    # Return JSON response
    return jsonify(response)
