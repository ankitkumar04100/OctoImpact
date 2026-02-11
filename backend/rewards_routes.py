from flask import Blueprint, request, jsonify

rewards_bp = Blueprint('rewards', __name__)
rewards = []

@rewards_bp.route("/rewards/add", methods=["POST"])
def add_reward():
    data = request.get_json()
    rewards.append({
        "user": data.get("user"),
        "points": data.get("points"),
        "nft_uri": data.get("nft_uri")
    })
    return jsonify({"message": "Reward added successfully", "total_rewards": len(rewards)})

@rewards_bp.route("/rewards", methods=["GET"])
def get_rewards():
    return jsonify(rewards)
