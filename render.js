const btn = document.getElementById("runBtn");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const tableBody = document.querySelector("#treeTable tbody");

btn.onclick = async () => {
  const n = parseInt(document.getElementById("treeCount").value);

  const res = await fetch("http://127.0.0.1:5000/pack", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ n })
  });

  const data = await res.json();
  drawPacking(data);
  fillTable(data);
};

function drawPacking(data) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const side = data.square_side;
  const scale = canvas.width / side;

  // Container square
  ctx.strokeStyle = "#22c55e";
  ctx.lineWidth = 2;
  ctx.strokeRect(0, 0, side * scale, side * scale);

  data.trees.forEach(tree => {
    drawTree(
      tree.x * scale,
      tree.y * scale,
      tree.rotation
    );
  });
}

function drawTree(x, y, angle) {
  ctx.save();
  ctx.translate(x + 10, y + 10);
  ctx.rotate(angle * Math.PI / 180);

  ctx.fillStyle = "#4ade80";
  ctx.beginPath();
  ctx.moveTo(0, -10);
  ctx.lineTo(8, 10);
  ctx.lineTo(-8, 10);
  ctx.closePath();
  ctx.fill();

  ctx.restore();
}

/* 🔽 TABLE LOGIC */

function fillTable(data) {
  tableBody.innerHTML = "";

  data.trees.forEach((tree, i) => {
    // Known triangle dimensions from geometry.py
    const width = 1.0;
    const height = 1.2;

    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${i + 1}</td>
      <td>${tree.x.toFixed(3)}</td>
      <td>${tree.y.toFixed(3)}</td>
      <td>${tree.rotation.toFixed(2)}</td>
      <td>${width}</td>
      <td>${height}</td>
    `;

    tableBody.appendChild(row);
  });
}
