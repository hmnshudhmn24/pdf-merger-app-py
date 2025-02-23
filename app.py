import os
from flask import Flask, render_template, request, send_file, redirect, url_for
from PyPDF2 import PdfMerger
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
MERGED_FOLDER = "merged_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MERGED_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MERGED_FOLDER"] = MERGED_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pdf_files = request.files.getlist("pdf_files")

        if not pdf_files:
            return "No files uploaded!", 400

        merger = PdfMerger()
        file_paths = []

        for file in pdf_files:
            if file.filename.endswith(".pdf"):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(file_path)
                file_paths.append(file_path)
                merger.append(file_path)

        merged_filename = "merged_document.pdf"
        merged_path = os.path.join(app.config["MERGED_FOLDER"], merged_filename)
        merger.write(merged_path)
        merger.close()

        return redirect(url_for("download_file", filename=merged_filename))

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    return send_file(os.path.join(app.config["MERGED_FOLDER"], filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
