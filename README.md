# Automated PDF Merger

This is a simple Flask-based web application that allows users to upload multiple PDF files and merge them into a single document.

## Features
- Upload multiple PDFs and merge them into one.
- Uses Flask for the web interface and PyPDF2 for merging PDFs.
- Download the merged PDF with a single click.

## Installation

1. Clone the repository or unzip the project folder.
2. Install dependencies:
   ```bash
   pip install flask PyPDF2 werkzeug
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## Folder Structure

```
pdf_merger/
├── app.py
├── templates/
│   ├── index.html
├── static/
│   ├── style.css
├── uploads/ (Stores uploaded PDFs)
├── merged_pdfs/ (Stores merged PDFs)
├── README.md
```

## License
This project is for educational purposes and is free to use.
