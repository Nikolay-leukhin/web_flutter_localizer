from flask import Flask, request, send_file, render_template
from localizer import Localizer
import os

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html', files=None)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'csv_file' not in request.files:
        return "No file part"

    file = request.files['csv_file']
    key_column = request.form['key_column']

    if file.filename == '':
        return "No selected file"

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        localizer = Localizer(file_path, key_column)
        generated_files = localizer.load_all_files(OUTPUT_FOLDER)
        return render_template('index.html', files=generated_files)
    except Exception as e:
        return f"Error: {e}"


@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    else:
        return "File not found."


if __name__ == '__main__':
    app.run(debug=True)
