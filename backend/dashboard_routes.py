from flask import Blueprint, jsonify
from ai_module import get_sustainability_insight

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/dashboard", methods=["GET"])
def get_dashboard():
    data = {
        "energy_saved": "12 kWh",
        "water_saved": "45 liters",
        "eco_score": 78,
        "ai_insight": get_sustainability_insight()
    }
    return jsonify(data)
