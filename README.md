#PDF and Image Merger App#

This is a Flask-based web application that allows users to merge multiple PDF files and images (JPG, JPEG) into a single PDF document. The app is designed for easy use and runs locally on your machine.
Features

- PDF Merging: Combine multiple PDF files into one.
- Image Conversion: Convert images (JPG, JPEG) into PDF and merge them with other PDFs.
- In-Memory Processing: All file processing is done in-memory for faster and safer file handling.
- Real-Time Flash Messages: User-friendly error handling with flash messages.

Demo

Installation

To set up the app on your local machine, follow these steps:
Prerequisites

Make sure you have the following installed:

        Python 3.x
        pip (Python package manager)
    
##Setup##

1. Clone the repository:
   
        git clone https://github.com/your-username/pdf-image-merger-app.git
        cd pdf-image-merger-app

3. Create a virtual environment (optional but recommended):

        python -m venv venv
        source venv/bin/activate   # On Windows, use `venv\Scripts\activate

3. Install the dependencies:

        pip install -r requirements.txt

4. Set up environment variables:

Create a .env file in the root directory and add your secret key:
        
        SECRET_KEY=your_secret_key_here

5. Run the application:

        python app.py

6. Open your browser and go to http://127.0.0.1:5000/ to access the app.

