<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"> <img src="https://img.shields.io/badge/Category-Automation-orange?style=for-the-badge"> </p>

## Email Extractor

A simple Python automation script that reads a text file, extracts all email addresses using regex, and saves them to an output file. Built with clean OOP design and basic file handling. Perfect for beginners learning Python automation.

## ✨ Key Features
- 📄 Reads input from any .txt file

- 🔍 Extracts all valid email addresses using regex

- 💾 Saves extracted emails to a separate output file

- 🧱 Clean Object-Oriented design with EmailExtractor class

- ⚠️ Error handling for missing input files

## 📁 Project Files
```bash
Email_Extractor.py   # Main OOP implementation and program entry point
README.md            # Project documentation
```

## 🚀 Getting Started
**1.** Make sure Python 3.x is installed:
```bash
python --version
```
**2.** Place your input file (e.g., `input.txt`) in the project directory.

**3.** Run the Program
```bash
python Email_Extractor.py
```

**4.** Extracted emails will be saved to `emails_output.txt`.

## 🧱 Code Structure (OOP)
| Class / Method     | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| **EmailExtractor** | Handles reading, extracting, and saving emails |
| `read_file()`      | Reads the content of the input file            |
| `extract_emails()` | Finds all email addresses using regex          |
| `save_emails()`    | Writes emails to the output file               |
| `run()`            | Coordinates reading, extracting, and saving    |

## 🧾 Example Output (Preview)
```text
📄 Reading file...
🔍 Extracting emails...
💾 Saving results...
✅ Extracted 15 emails and saved to: emails_output.txt
🎉 Task Completed!
```

## 🧰 Customization
- Change input/output file names:
```python
extractor = EmailExtractor("my_input.txt", "my_emails.txt")
extractor.run()
```
- Modify regex for custom email formats if needed.

## 🤝 Contributing
Enhance this project by adding features like:

- Support for multiple input files

- GUI interface (Tkinter / PyQt)

- Export to CSV or Excel

## 📜 License
This project is free to use, modify, and share.
