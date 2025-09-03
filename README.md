# Website Status Checker

A simple Python script that checks if websites are online.  
It reads URLs from a text file, verifies their status, and saves a report. This project is beginner-friendly and demonstrates Python skills in **functions, file handling, loops, and error handling**.

---

## Features
- Checks multiple websites at once.
- Detects online/offline websites.
- Handles errors gracefully.
- Saves results to a report file (`status_report.txt`).
- Allows the user to specify the input text file interactively.

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/website-status-checker.git
```
2. **Navigate into the folder:**
```bash
cd website-status-checker
```
3. **Install dependencies:**
```bash
pip install requests
```

---

## Usage

1. **Prepare a text file with website URLs, one per line. You can use the provided websites_sample.txt.**
Example:
```arduino
https://www.google.com
https://www.github.com
https://www.python.org
```
2. **Run the script:**
```bash
python website_status_checker.py
```
3. **Enter the filename when prompted:**
```pgsql
Enter the name of the text file with website URLs (e.g., websites.txt):
```
4. **The program will check each website and display the results in the terminal.**
5. **Results are also saved to status_report.txt automatically.**

---

## Example Output

```csharp
Enter the name of the text file with website URLs: websites_sample.txt
https://www.google.com is online.
https://www.github.com is online.
https://fakewebsite1234.com is unreachable.

Results saved to 'status_report.txt'.
```
