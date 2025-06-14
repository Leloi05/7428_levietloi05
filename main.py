import streamlit as st
st.title('hello world')
<!DOCTYPE html>
<html>
<head>
  <title>🏁 Game Đua Xe</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      background: #333;
    }

    canvas {
      display: block;
      margin: auto;
      background: #111;
    }
  </style>
</head>
<body>
<canvas id="gameCanvas" width="400" height="600"></canvas>

<script>
  const canvas = document.getElementById('gameCanvas');
  const ctx = canvas.getContext('2d');

  const car = {
    x: 180,
    y: 500,
    width: 40,
    height: 70,
    color: 'red',
    moveLeft: false,
    moveRight: false,
  };

  const obstacles = [];

  function drawCar() {
    ctx.fillStyle = car.color;
    ctx.fillRect(car.x, car.y, car.width, car.height);
  }

  function drawObstacles() {
    ctx.fillStyle = 'white';
    for (let obs of obstacles) {
      ctx.fillRect(obs.x, obs.y, obs.width, obs.height);
    }
  }

  function updateObstacles() {
    for (let obs of obstacles) {
      obs.y += 4;
    }
    if (Math.random() < 0.02) {
      obstacles.push({
        x: Math.random() * 360,
        y: -30,
        width: 40,
        height: 60
      });
    }
  }

  function detectCollision() {
    for (let obs of obstacles) {
      if (
        car.x < obs.x + obs.width &&
        car.x + car.width > obs.x &&
        car.y < obs.y + obs.height &&
        car.y + car.height > obs.y
      ) {
        return true;
      }
    }
    return false;
  }

  function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (car.moveLeft && car.x > 0) car.x -= 5;
    if (car.moveRight && car.x < canvas.width - car.width) car.x += 5;

    updateObstacles();
    drawObstacles();
    drawCar();

    if (detectCollision()) {
      alert("💥 Game Over! Refresh để chơi lại.");
      document.location.reload();
    } else {
      requestAnimationFrame(gameLoop);
    }
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') car.moveLeft = true;
    if (e.key === 'ArrowRight') car.moveRight = true;
  });

  document.addEventListener('keyup', (e) => {
    if (e.key === 'ArrowLeft') car.moveLeft = false;
    if (e.key === 'ArrowRight') car.moveRight = false;
  });

  gameLoop();
</script>
</body>
</html>

