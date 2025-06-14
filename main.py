import streamlit as st
st.title('hello world')
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🎉 Trang Web Giải Trí</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      background: linear-gradient(to bottom, #000000, #2c3e50);
      animation: bg 10s infinite alternate;
      font-family: 'Segoe UI', sans-serif;
    }

    @keyframes bg {
      0% { background: linear-gradient(to bottom, #000000, #2c3e50); }
      100% { background: linear-gradient(to bottom, #1e3c72, #2a5298); }
    }

    h1 {
      color: white;
      text-align: center;
      margin-top: 40px;
      font-size: 3em;
      text-shadow: 0 0 10px pink;
    }

    .heart {
      width: 20px;
      height: 20px;
      background-color: pink;
      position: absolute;
      top: 100%;
      transform: rotate(45deg);
      animation: float 4s linear infinite;
    }

    .heart::before,
    .heart::after {
      content: "";
      width: 20px;
      height: 20px;
      background-color: pink;
      border-radius: 50%;
      position: absolute;
    }

    .heart::before {
      top: -10px;
      left: 0;
    }

    .heart::after {
      left: -10px;
      top: 0;
    }

    @keyframes float {
      0% {
        transform: translateY(0) rotate(45deg);
        opacity: 1;
      }
      100% {
        transform: translateY(-600px) rotate(45deg);
        opacity: 0;
      }
    }

    .credit {
      position: absolute;
      bottom: 10px;
      width: 100%;
      text-align: center;
      color: white;
      font-size: 0.9em;
    }

    audio {
      display: none;
    }
  </style>
</head>
<body>

  <h1>💖 Chào mừng bạn đến với thế giới giải trí! 💖</h1>

  <!-- Nhạc nền tự động phát -->
  <audio autoplay loop>
    <source src="https://www.bensound.com/bensound-music/bensound-ukulele.mp3" type="audio/mpeg">
  </audio>

  <div class="credit">🎵 Nhạc nền: Bensound – Ukulele | Hiệu ứng by ChatGPT 💫</div>

  <script>
    setInterval(() => {
      const heart = document.createElement('div');
      heart.className = 'heart';
      heart.style.left = Math.random() * window.innerWidth + 'px';
      heart.style.animationDuration = (3 + Math.random() * 2) + 's';
      document.body.appendChild(heart);
      setTimeout(() => heart.remove(), 5000);
    }, 200);
  </script>

</body>
</html>
