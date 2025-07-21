# ❓ Quiz Game – Python (API + GUI)

This is a quiz application built with Python that fetches trivia questions from an online API and presents them to the user through a graphical interface using Tkinter.

The app tracks the user's score and gives immediate visual feedback for correct and incorrect answers.

---

## 🎯 Features

- Live question fetching from the Open Trivia DB API
- Multiple choice questions with True/False format
- Color feedback (green/red) for correct or wrong answers
- Score tracking during the game
- Responsive and clean GUI using Tkinter

---

## 🧠 Technologies & Concepts

- **Python 3**
- **Tkinter** – for GUI layout and control
- **requests** – for making API calls
- **Class-based architecture**:
  - `QuizBrain`: handles quiz logic and flow
  - `UI`: manages the interface and user input
  - `QuestionModel`: represents a single question object

---

## 🗂️ File Structure

```
Quiz-API-GUI/
├── main.py               # Initializes the app and UI
├── quiz_brain.py         # Quiz logic: fetching, validating answers
├── ui.py                 # GUI layout using Tkinter
├── question_model.py     # Defines the question object structure
├── data.py               # Handles API connection (or sample data)
└── images/
    ├── true.png
    └── false.png
```

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Install dependencies (only `requests` if not already installed):

```bash
pip install requests
```

3. Run the app:

```bash
python main.py
```

---

## 🚀 Possible Improvements

- Add support for multiple categories or difficulty selection
- Implement a restart button or menu
- Use different APIs or allow offline question sets
- Track high scores across sessions

---

## 📚 API Reference

Uses the [Open Trivia DB API](https://opentdb.com/api_config.php) to fetch trivia questions dynamically.

---

## 🙋‍♂️ Author

Created by **Amir Hartman** as a self-learning project in Python GUI and API integration.

---

## 🧾 License

This project is open for educational and personal use. Feel free to extend or modify it.
