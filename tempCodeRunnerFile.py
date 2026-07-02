# 🎮 Connect Four AI Game

A Python implementation of the classic **Connect Four** game built with **Pygame** and **NumPy**. Play against an AI opponent that uses the **Minimax algorithm with Alpha-Beta Pruning** to make intelligent decisions.

---

## 📌 Project Overview

This project recreates the classic Connect Four board game where a human player competes against an AI. The AI analyzes possible future moves using the Minimax algorithm and optimizes its search using Alpha-Beta Pruning.

The game provides a graphical interface using Pygame and follows the standard Connect Four rules.

---

## ✨ Features

- Interactive graphical interface using Pygame
- Human vs AI gameplay
- Intelligent AI using:
  - Minimax Algorithm
  - Alpha-Beta Pruning
- Win detection
  - Horizontal
  - Vertical
  - Diagonal
- Board evaluation heuristic
- Center-column preference strategy
- Smooth gameplay with AI thinking delay

---

## 🧠 AI Algorithm

The computer opponent uses:

- **Minimax Search**
  - Explores possible future game states.
  - Maximizes the AI score while minimizing the player's score.

- **Alpha-Beta Pruning**
  - Eliminates branches that cannot affect the final decision.
  - Improves performance by reducing unnecessary computations.

- **Heuristic Evaluation**
  - Rewards:
    - Four in a row
    - Three connected pieces
    - Two connected pieces
    - Center column control
  - Penalizes dangerous player positions.

---

## 🛠 Technologies Used

- Python 3
- Pygame
- NumPy
- Math
- Random

---

## 📂 Project Structure

```
ConnectFour/
│
├── connect_four.py
├── README.md
└── requirements.txt
```

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/connect-four-ai.git
```

### 2. Navigate to the project

```bash
cd connect-four-ai
```

### 3. Install dependencies

```bash
pip install pygame numpy
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Game

Run:

```bash
python connect_four.py
```

The game window will open automatically.

---

## 🎮 How to Play

- You are **Player 1 (Red pieces)**.
- The AI plays as **Yellow pieces**.
- Click on a column to drop your piece.
- The first player to connect **4 pieces** horizontally, vertically, or diagonally wins.
- If the board fills without a winner, the game ends in a draw.

---

## 📊 Game Rules

- The board has **6 rows** and **7 columns**.
- Players take turns dropping one piece at a time.
- Pieces always occupy the lowest available space in a column.
- Four consecutive pieces wins the game.

---

## 🧩 Main Functions

| Function | Description |
|----------|-------------|
| `create_board()` | Creates the game board |
| `drop_piece()` | Places a piece on the board |
| `winning_move()` | Checks if a player has won |
| `score_position()` | Evaluates the current board |
| `evaluate_window()` | Scores groups of four cells |
| `minimax()` | AI decision-making algorithm |
| `draw_board()` | Renders the game board |
| `get_valid_locations()` | Returns available columns |

---

## 📸 Gameplay

- Human player uses the mouse to choose a column.
- The AI calculates the best move.
- The board updates after every turn.
- A victory message is displayed when someone wins.

---

## 🚀 Future Improvements

- Difficulty levels (Easy, Medium, Hard)
- Multiplayer mode
- Restart button
- Score tracking
- Sound effects
- Animated piece dropping
- Better AI evaluation
- Draw detection message
- Main menu interface

---

## 📚 Concepts Demonstrated

- Artificial Intelligence
- Minimax Algorithm
- Alpha-Beta Pruning
- Heuristic Search
- Game Development
- Event Handling
- Object-Oriented Programming Concepts
- Matrix Manipulation using NumPy

---

## 👩‍💻 Author

**Mariam Essam**

---

## 📄 License

This project is intended for educational and learning purposes.