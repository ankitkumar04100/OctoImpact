# backend/dashboard_routes.py
from flask import Blueprint, jsonify
import pandas as pd
from .ai_module import generate_sustainability_insights

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/api/dashboard')
def get_dashboard_data():
    data = pd.DataFrame({
        'User': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Energy_Saved_kWh': [12, 8, 15, 9, 11],
        'Water_Saved_Liters': [45, 30, 60, 50, 42],
        'Eco_Score': [78, 65, 85, 70, 80]
    })
    data = generate_sustainability_insights(data)
    return jsonify(data.to_dict(orient='records'))
