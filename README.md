# 🐍 Snake Game (Python – Turtle Graphics)

A classic Snake game built using Python's built-in **turtle** graphics module.  
This project is simple, lightweight, and great for learning object-oriented programming, event handling, and basic game logic in Python.

---


---

## 🚀 Features

- Smooth snake movement  
- Food items that spawn at random locations  
- Score tracking  
- **Difficulty selection (Easy / Medium / Hard)**  
- Collision detection (walls + tail)  
- Simple, modular object-oriented code  
- Built entirely with the standard Python library (no external dependencies)

---

## 📁 Project Structure
Snake-Game/
│
├── main.py # Main game loop
├── snake.py # Snake class (movement & body segments)
├── food.py # Food class (random repositioning)
├── scoreboard.py # Scoreboard class (score + game over text)
└── README.md # Project documentation

---

## 🧠 How to Play

| Key | Action |
|-----|--------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

### Objective  
Eat as many food items as possible.  
Each piece of food increases your score **and** grows the snake.

### Game Over Conditions  
- Snake hits a wall  
- Snake collides with its own tail

## 🎚️ Difficulty Levels

When you run the game, you will be prompted to choose:

- **easy** → Slow movement  
- **medium** → Balanced speed  
- **hard** → Fast, challenging gameplay  

This is implemented by adjusting the movement delay of the snake.

Example logic:

```python
difficulty = screen.textinput("Difficulty", "Choose: easy / medium / hard")
speed = {"easy": 0.15, "medium": 0.1, "hard": 0.05}.get(difficulty, 0.1)
```
---

## 🛠️ Installation & Setup

### **1. Ensure you have Python installed**
Check with:


```bash
python --version
```

2. Clone the repository


3. Run the game
python main.py

## 🧩 Code Overview

### **main.py**
- Sets up the screen  
- Handles event listeners  
- Runs the game loop  

### **snake.py**
- Creates the snake body  
- Handles movement and turning logic  
- Adds new segments when food is eaten  

### **food.py**
- Randomly positions food on the game field  
- Uses a small turtle-shaped sprite  

### **scoreboard.py**
- Tracks and displays the current score  
- Prints GAME OVER when the game ends  

📜 License
This project is intended for educational, academic, and portfolio demonstration purposes.
For commercial or corporate use, please request permission.

🤝 Contributing

Pull requests and suggestions are welcome!

💡 Author

Created by C Sindhu Sharma
If you enjoy the project, consider ⭐ starring the repository on GitHub!








