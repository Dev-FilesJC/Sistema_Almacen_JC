# Se ejecuta dentro del espacio global de app.py para conservar compatibilidad.
import streamlit as st

st.subheader("🦖 Dinosaurio Saltarín ☁️")

# Botón de reinicio
if st.button("🔄 Reiniciar Juego"):
    st.rerun()

game_code = """
<style>
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: black;
}

#gameContainer {
    width: 100%;
    height: 100%;
    background-color: black;
}

canvas {
    display: block;
    width: 100%;
    height: 100%;
    background-color: #cce7ff;  /* Día por defecto */
    border: 2px solid #333;
}
</style>

<div id="gameContainer">
<canvas id="gameCanvas"></canvas>
</div>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

function resizeCanvas() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
}
resizeCanvas();
window.addEventListener("resize", resizeCanvas);

ctx.textBaseline = "bottom";

let groundLevel = canvas.height - 20;

let dino = {
    x: 50, y: groundLevel - 40, width: 40, height: 40,
    dy: 0, gravity: 1, jumpPower: -15, grounded: true
};

let obstacles = [
    { x: 800, width: 20, height: 40, type: "smallCactus", speed: 6 },
    { x: 1200, width: 30, height: 60, type: "bigCactus", speed: 6 },
    { x: 1600, width: 30, height: 30, type: "bird", speed: 8 }
];

// Ajustar posición inicial
obstacles.forEach(o => {
    if (o.type === "bird") {
        o.y = groundLevel - o.height - 60;
    } else {
        o.y = groundLevel - o.height;
    }
});

// Nubes decorativas ☁️
let clouds = [
    { x: 100, y: 50, speed: 1 },
    { x: 400, y: 80, speed: 0.8 },
    { x: 700, y: 60, speed: 1.2 }
];

function drawClouds() {
    ctx.font = "30px Arial";
    clouds.forEach(c => {
        ctx.fillText("☁️", c.x, c.y);
    });
}

function updateClouds() {
    clouds.forEach(c => {
        c.x -= c.speed;
        if (c.x < -50) {
            c.x = canvas.width + Math.random() * 200;
            c.y = 30 + Math.random() * 60;
        }
    });
}

// Día y noche 🌞🌙
let isDay = true;

function updateBackgroundColor() {
    if (score % 20 === 0 && score !== 0 && score !== lastToggleScore) {
        isDay = !isDay;
        lastToggleScore = score;
    }

    if (isDay) {
        canvas.style.backgroundColor = "#cce7ff";  // Día
    } else {
        canvas.style.backgroundColor = "#2c3e50";  // Noche
    }
}

let gameOver = false;
let score = 0;
let lastToggleScore = -1;

function drawBackground() {
    ctx.fillStyle = "#8B4513";
    ctx.fillRect(0, canvas.height - 20, canvas.width, 20);
}

function drawDino() {
    ctx.font = "40px Arial";
    ctx.fillText("🦖", dino.x, dino.y + dino.height);
}

function drawObstacles() {
    ctx.font = "40px Arial";
    obstacles.forEach(o => {
        if (o.type === "smallCactus" || o.type === "bigCactus") {
            ctx.fillText("🌵", o.x, o.y + o.height);
        } else if (o.type === "bird") {
            ctx.fillText("🐦", o.x, o.y + o.height);
        }
    });
}

function update() {
    if (gameOver) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    updateBackgroundColor();  // Cambiar día/noche
    updateClouds();
    drawBackground();
    drawClouds();

    groundLevel = canvas.height - 20;

    // Dino saltando
    dino.y += dino.dy;
    if (dino.y + dino.height < groundLevel) {
        dino.dy += dino.gravity;
        dino.grounded = false;
    } else {
        dino.y = groundLevel - dino.height;
        dino.dy = 0;
        dino.grounded = true;
    }

    // Obstáculos
    obstacles.forEach(o => {
        o.x -= o.speed;
        if (o.x + o.width < 0) {
            o.x = canvas.width + Math.random() * 400;

            if (o.type === "bird") {
                o.y = groundLevel - o.height - 60;
            } else {
                o.y = groundLevel - o.height;
            }

            score++;
            if (score % 5 === 0) o.speed += 1;
        }

        // Colisión
        if (
            dino.x < o.x + o.width &&
            dino.x + dino.width > o.x &&
            dino.y < o.y + o.height &&
            dino.y + dino.height > o.y
        ) {
            gameOver = true;
            alert("💀 Game Over! Fuck you Puntuación final: " + score);
        }
    });

    drawDino();
    drawObstacles();

    ctx.fillStyle = isDay ? "black" : "white";
    ctx.font = "20px Arial";
    ctx.fillText("Score: " + score, 10, 30);

    requestAnimationFrame(update);
}

window.addEventListener("keydown", function(e) {
    if ((e.code === "Space" || e.code === "ArrowUp") && dino.grounded) {
        dino.dy = dino.jumpPower;
    }
});

update();
</script>
"""

st.components.v1.html(game_code, height=450)
