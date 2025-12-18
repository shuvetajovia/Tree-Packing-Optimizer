🎄 Tree Packing Optimizer

**ML-Assisted Geometric Optimization & Visualization**

📌 Overview

Tree Packing Optimizer is a full-stack machine learning and geometry project that computes the **optimal placement of Christmas tree toys inside the smallest possible square box**.

Given only the **number of trees**, the system:

* predicts optimal rotation angles using ML,
* arranges trees without overlap using geometric heuristics,
* minimizes the bounding square area,
* and visualizes the result interactively in the browser.

This project was inspired by optimization challenges such as **packing, layout planning, and spatial efficiency problems**.

---

🎯 Problem Statement

Santa needs to pack between **1–200 Christmas tree toys** into a **square parcel** using minimal space.

Each tree:

* has a fixed shape,
* can be rotated,
* must not overlap with others.

The challenge is to **minimize the square box size** while fitting all trees.

---

🧠 Solution Approach

### 1️⃣ Machine Learning (Rotation Prediction)

* A **RandomForestRegressor** is trained on historical packing data.
* Input: number of trees (`n`)
* Output: optimal rotation angle (degrees)
* Purpose: guide the optimizer toward better layouts faster.

### 2️⃣ Geometry & Optimization

* Trees are modeled as **polygons (triangular shapes)**.
* Trees are placed on a grid with:

  * rotation candidates,
  * overlap detection using **Shapely**,
  * multiple heuristic trials.
* The **best solution** is chosen based on the smallest bounding square.

### 3️⃣ Visualization

* HTML5 Canvas renders:

  * each tree as a triangle,
  * the bounding square,
  * real-time layout updates.
* A table displays:

  * X & Y coordinates,
  * rotation,
  * estimated width & height per tree.

---

🧩 Project Architecture


tree-packing-optimizer/
│
├── backend/
│   ├── api.py           # Flask API
│   ├── optimizer.py    # Heuristic optimization logic
│   ├── packer.py       # Tree placement & collision checks
│   ├── geometry.py     # Polygon math utilities
│   └── model.pkl       # Trained ML model
│
├── frontend/
│   ├── index.html      # UI + table
│   ├── style.css       # Styling
│   └── render.js       # Canvas + API integration
│
├── assets/
│   └── screenshots/    # Project visuals
│
├── requirements.txt
└── README.md


---

🚀 How It Works (End-to-End)

1. User opens `index.html`
2. Enters **number of trees**
3. Frontend sends `POST /pack`
4. Backend:

   * ML predicts rotation
   * Optimizer computes placement
5. Backend returns coordinates
6. Frontend:

   * draws trees on canvas
   * fills placement table

Result: optimized packing visualized instantly.

---

🛠️ Technologies Used

* **Python**
* **Flask** (API)
* **scikit-learn** (ML)
* **Shapely** (Computational Geometry)
* **HTML5 Canvas**
* **JavaScript**
* **CSS**

---

📦 Installation & Run

### Backend

```bash
cd backend
pip install -r requirements.txt
python api.py
```

Server runs at:

```
http://127.0.0.1:5000
```

### Frontend

Simply open:

```
frontend/index.html
```

in a browser.

---

📊 Output Details

For each tree, the system provides:

* X position
* Y position
* Rotation angle
* Estimated width
* Estimated height

All results are visualized **and** tabulated.

---

💡 Applications

This project demonstrates concepts applicable to:

* warehouse & container packing
* VLSI chip placement
* urban planning layouts
* resource optimization
* computational geometry problems

---

🏆 Highlight

> Built a full-stack ML-assisted geometric optimization system to minimize spatial usage while packing multiple objects,
> integrating machine learning, heuristic search, and real-time visualization.

---

📜

For educational and research use.

---
