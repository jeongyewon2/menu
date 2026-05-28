# 한밭대학교 학생생활관 식단표 조회 프로그램 (Hanbat National University Dormitory Meal Schedule Viewer)

---

## Abstract

The **Hanbat National University Dormitory Meal Schedule Viewer** is a Python-based desktop application developed to address the inconvenience faced by dormitory residents who need to check weekly meal schedules posted on the university's official dormitory website. Rather than requiring students to navigate a web browser and manually parse HTML-rendered tables each time, this program automates the entire workflow via real-time web scraping (using `requests` and `BeautifulSoup`) and presents the extracted data in a clean, interactive GUI window built with Python's standard `tkinter` library. The application eliminates the friction of repeated manual lookups and provides an intuitive interface optimized for quick meal-planning decisions.

---

## Key Features

- **Real-Time Web Scraping** — Fetches the latest weekly meal schedule directly from the official dormitory website (`dorm.hanbat.ac.kr`) on every launch, ensuring the displayed information is always up to date.

- **Automatic Day Detection** — On startup, the program automatically detects the current day of the week from the system clock and immediately displays the corresponding menu without requiring any user input.

- **Interactive Day Selection** — A drop-down combo box allows users to freely switch between Monday through Sunday to browse the full weekly menu at their convenience.

- **Robust Error Handling** — Network failures, server timeouts, vacation periods, and missing table data are gracefully caught with `try-except` blocks. User-friendly warning and error dialog boxes (`messagebox`) are displayed instead of program crashes.

- **Clean & Readable Output** — All raw HTML tags are stripped via BeautifulSoup's parser, and extraneous whitespace is normalized. Menu items are formatted with bullet points under clearly labeled meal periods (Breakfast / Lunch / Dinner) inside a scrollable text widget.

---

## Getting Started

### Prerequisites

- **Python 3.9 or higher** installed on your system.  
  Download from [python.org](https://www.python.org/downloads/) if not already installed.
- An active internet connection (required for the initial data fetch).

### Installation & Setup

1. **Clone or download this repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/hanbat-dorm-meal-viewer.git
   cd hanbat-dorm-meal-viewer
   ```

   > If you do not use Git, download the ZIP archive from GitHub, extract it, and open a terminal in the extracted directory.

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   ```

   Activate the environment:

   - **Windows (Command Prompt)**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS / Linux**
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   This installs `requests` (HTTP client) and `beautifulsoup4` (HTML parser) at their latest stable versions.

### Run

```bash
python main.py
```

A GUI window titled **"한밭대학교 학생생활관 식단표"** will open. The current day's menu is displayed automatically. Use the drop-down menu to switch between days, or click **"새로고침"** (Refresh) to re-fetch the data from the server.
