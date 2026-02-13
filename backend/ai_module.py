# backend/ai_module.py
import pandas as pd
import numpy as np
import random

def generate_sustainability_insights(user_data):
    insights = [
        "Reduce daily water usage by 10%",
        "Use energy-efficient appliances",
        "Recycle at least 3 types of waste weekly",
        "Plant a tree every month",
        "Opt for public transport to reduce carbon footprint"
    ]
    user_data['AI_Insight'] = [random.choice(insights) for _ in range(len(user_data))]
    return user_data
