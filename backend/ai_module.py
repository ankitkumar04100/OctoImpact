import random
from config import Config

def get_sustainability_insight():
    insights = [
        "Reduce daily water usage by 10%",
        "Use energy-efficient appliances",
        "Recycle at least 3 types of waste every week",
        "Plant a tree every month",
        "Opt for public transport to reduce carbon footprint"
    ]
    return random.choice(insights)
