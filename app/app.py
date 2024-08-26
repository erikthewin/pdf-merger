import os
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
from PyPDF2 import PdfMerger
from PIL import Image
from io import BytesIO

ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') # Set a secret key for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_files():
    # Create a PdfMerger object
    pdf_merger = PdfMerger()

    # Get the uploaded files from the request
    files = request.files.getlist('files')

    # Merge the files in-memory
    for file in files:
        if file and allowed_file(file.filename):
            # Check file type
            filename = secure_filename(file.filename)
            if filename.lower().endswith('.pdf'):
                # If PDF, append directly to PdfMerger
                pdf_merger.append(file)
            elif filename.lower().endswith(('.jpg', '.jpeg')):
                # If JPG, convert to PDF and append to PdfMerger
                img = Image.open(file)
                pdf_bytes = BytesIO()
                img.save(pdf_bytes, format='PDF')
                pdf_bytes.seek(0)
                pdf_merger.append(pdf_bytes)

    if not pdf_merger.pages:
        flash("No valid files uploaded. Please upload valid PDF or image files.")
        return redirect(url_for('index'))

    # Save the merged PDF to an in-memory BytesIO object
    output_stream = BytesIO()
    pdf_merger.write(output_stream)
    output_stream.seek(0)

    # Return the merged PDF as a response, with as_attachment=False to display inline
    return send_file(output_stream, as_attachment=False, mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
