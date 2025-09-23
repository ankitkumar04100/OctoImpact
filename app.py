from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/insights', methods=['GET'])
def get_insights():
    return jsonify({"message": "AI insights coming soon!"})

if __name__ == "__main__":
    app.run(debug=True)
