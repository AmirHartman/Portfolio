# 🔐 Password Manager – Python (GUI)

A simple desktop application to manage website credentials with a built-in secure password generator.  
The app allows users to generate and store passwords in a local JSON file and retrieve them when needed.

---

## 🔑 Features

- Generate strong, random passwords
- Save credentials (website, username, password)
- Search for existing saved entries
- Copy generated password to clipboard
- Friendly GUI built using Tkinter

---

## 🧠 Technologies & Concepts

- **Python 3**
- **Tkinter** – for the GUI interface
- **JSON** – local file-based data storage
- **pyperclip** (optional) – for clipboard copy functionality
- Input validation, modular design, basic file handling

---

## 🗂️ File Structure

```
Password-Manager-GUI/
├── main.py            # Full application logic and GUI
├── data.json          # Saved credentials (auto-created)
├── logo.png           # App icon (if used)
└── README.md
```

---

## ▶️ How to Run

1. Install Python 3  
2. (Optional) Install clipboard helper:
```bash
pip install pyperclip
```

3. Run:
```bash
python main.py
```

---

## ⚠️ Security Note

Passwords are saved **unencrypted** in a local file (`data.json`).  
For production use, consider encrypting data or using a password vault API.

---

## 🙋‍♂️ Author

Built by **Amir Hartman** as part of a self-learning project in GUI and data storage with Python.

---

## 🧾 License

This is an open educational project. Modify and use as needed.
