**NUMBER GUESSING GAME IN PYTHON**

A customizable CLI game that demonstrates core Python programming concepts with clean, maintainable code.


# 🚀 Features
- **3 Difficulty Levels** (Easy/Medium/Hard) with adaptive number ranges
- **Attempt Tracking** with remaining guesses counter
- **Input Validation** prevents crashes from non-number inputs
- **User-Friendly Interface** with emoji feedback
- **Pure Python** (No external dependencies used)

## 💻 How It Works
```python
# Core game logic snippet
def check_guess(secret, guess):
    if guess == secret:
        return "🎉 Correct!"
    return "⬆️ Higher!" if guess < secret else "⬇️ Lower!"

Developed with ❤️ by Shreshth Behal 
