# 📅 Work Scheduler – Google Sheets / Excel Automation

A semi-automated system for generating shift schedules using Microsoft Excel and Google Sheets.  
Built to reduce manual work in organizing employee shifts, with smart constraints and dropdown-based selections.

---

## ⚙️ Features

- Dropdown-based role and person assignment
- Conflict checking using cell validation
- Blocked time slots managed by a "חסימות" sheet
- Easily extendable and visual

---

## 📂 File Structure

```
Work-Scheduler-GoogleSheets/
├── חסימות.xlsx       # Input: blocked times by user
├── קובץ אם.xlsx      # Master logic + formulas
└── סידור.xlsx        # Final output: full schedule
```

---

## 🧠 Tools & Logic

- **Excel formulas** (e.g., `VLOOKUP`, `IF`, `COUNTIF`)
- **Data validation**
- **Dropdown lists**
- **Sheet references across multiple files**
- **Modular structure** to support multiple user types

---

## ✅ Use Case

Used successfully to generate work shifts in a real-world organization.  
Improved scheduling time by at least 50%.

---

## 🔄 Future Ideas

- Full automation via Google Apps Script or Python (e.g., `gspread`)
- UI for inserting constraints
- Auto-emailing final schedule to participants

---

## 🙋‍♂️ Author

Created by **Amir Hartman** to improve internal efficiency in scheduling shifts.

---

## 🧾 License

Files are shared for demonstration and learning purposes. Do not reuse with personal data.
