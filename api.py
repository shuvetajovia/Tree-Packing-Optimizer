from flask import Flask, request, jsonify
from flask_cors import CORS
from optimizer import optimize_packing
import joblib
import os

# -------------------- App Setup --------------------
app = Flask(__name__)
CORS(app)  # allow frontend requests

# -------------------- Model Loading --------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ ML model loaded successfully")
else:
    print("⚠️ model.pkl not found, running without ML guidance")

# -------------------- Helper --------------------
def get_rotation_hints(n):
    """
    Uses ML model to predict a good rotation angle.
    Returns list because optimizer expects iterable.
    """
    if model is None:
        return None

    # RandomForestRegressor -> single float
    rotation = float(model.predict([[n]])[0])

    # Clamp for stability
    rotation = max(60.0, min(150.0, rotation))

    return [rotation]

# -------------------- Routes --------------------
@app.route("/", methods=["GET"])
def health():
    return {
        "status": "Tree Packing Optimizer API running",
        "ml_loaded": model is not None
    }

@app.route("/pack", methods=["POST"])
def pack():
    data = request.get_json(force=True)

    n = int(data.get("n", 10))
    n = max(1, min(200, n))  # competition-safe

    rotation_hints = get_rotation_hints(n)

    result = optimize_packing(
        n=n,
        rotation_hints=rotation_hints,
        trials=8
    )

    response = {
        "square_side": round(result["side"], 4),
        "trees": [
            {
                "id": i,
                "x": round(p[0], 4),
                "y": round(p[1], 4),
                "rotation": round(p[2], 2)
            }
            for i, p in enumerate(result["placements"])
        ]
    }

    return jsonify(response)

# -------------------- Main --------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
