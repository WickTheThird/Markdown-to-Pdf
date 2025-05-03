# md_to_pdf Converter

A simple Python script to convert Markdown files to PDF using **markdown-it-py** and **WeasyPrint**.

## Features

- Parses Markdown with support for:
  - Tables
  - Fenced code blocks
  - Strikethrough
- Handles images and tables with proper styling and wrapping
- No external dependencies like `wkhtmltopdf`

## Installation

1. Clone the repository or download `converter.py` and this `requirements.txt`.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Change Name of file inside `converter.py` to desired file to change
4. Run `converter.py`:
   ```bash
   python converter.py
   ```
