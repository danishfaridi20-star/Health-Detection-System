from flask import Blueprint, request, jsonify
from app.services.ai_service import get_ai_response
import json

prediction_bp = Blueprint("prediction", __name__)

@prediction_bp.route("/predict", methods=["POST"])
def predict():


    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"})

 
    disease = data.get("disease")

 
    if not disease:
        return jsonify({"error": "Please enter disease"})

 
    response = get_ai_response(disease)

 
    response = json.loads(response)

 
    return jsonify(response)
