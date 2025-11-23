<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"> <img src="https://img.shields.io/badge/Category-Automation-orange?style=for-the-badge"> </p>

A simple, object-oriented Python script that extracts email addresses from a text file and saves them to another file. Built with clear OOP design, regex-based extraction, and basic file handling. Perfect for beginners learning automation with Python.

## ✨ Key Features
- 📄 Reads input from any .txt file

- 🔍 Extracts all valid email addresses using regex

- 💾 Saves extracted emails to a separate output file

- 🧱 Clean Object-Oriented structure:

  - EmailExtractor class → handles file reading, email extraction, and saving

  - run() method → coordinates the workflow

- ⚠️ Error handling for missing input files

## 📁 Project Files
```bash
Email_Extractor.py   # Main OOP implementation and program entry point
README.md            # Project documentation
```

## 🚀 Getting Started
### 1. Install Python

Ensure Python 3.x is installed. 
Check using:
```bash
python --version
```

### 2. Run the Program
```bash
python Email_Extractor.py
```

### 3. Use the Script
- Place your input .txt file in the same directory (default name: files.txt)

- The script will extract emails and save them to emails_output.txt

- You can change the file names by editing the script’s EmailExtractor instantiation

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

  Pull requests and forks are welcome!

## 📜 License
This project is free to use, modify, and share.
