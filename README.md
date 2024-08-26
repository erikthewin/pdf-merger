# PDF and Image Merger App #

This is a Flask-based web application that allows users to merge multiple PDF files and images (JPG, JPEG) into a single PDF document. The app is designed for easy use and runs locally on your machine.
Features

- PDF Merging: Combine multiple PDF files into one.
- Image Conversion: Convert images (JPG, JPEG) into PDF and merge them with other PDFs.
- In-Memory Processing: All file processing is done in-memory for faster and safer file handling.
- Real-Time Flash Messages: User-friendly error handling with flash messages.

## Demo ##

## Installation ##

To set up the app on your local machine, follow these steps:

### Prerequisites ###

Make sure you have the following installed:

        Python 3.x (if not running with docker)
        pip (Python package manager) (if not running with docker)
        Docker (optional)

### Setup with docker ###

1. Create a .env file

If your Flask application relies on environment variables (e.g., for configuration or secrets), create a .env file in your project root (same directory as the Dockerfile). Add your key-value pairs in this format:

        SECRET_KEY=your_secret_key

2. Build the Docker Image

Open a terminal in the project directory (where your Dockerfile is located) and build the Docker image:

        docker build -t flask-app .

3. Run the Docker Container

To run the Docker container, use the following command:

        docker run --env-file .env -p 5000:5000 flask-app

This command does the following:

    --env-file .env: Loads environment variables from your .env file into the container.
    -p 5000:5000: Maps port 5000 on your local machine to port 5000 on the container (where Flask will be running).
    flask-app: The name of the Docker image built in the previous step.

4. Access the Application

Once the container is running, you can access your Flask application by navigating to http://localhost:5000 in your web browser.
    
### Setup without docker ###

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

6. Open your browser and go to http://localhost:5000/ to access the app.

### Usage ###

    Upload Files: Drag and drop or select multiple PDF or image files (JPG, JPEG).
    Merge Files: Once the files are uploaded, they will be merged into a single PDF document.
    View Merged PDF: The merged PDF will be displayed in the browser for preview or download.

### File Types Supported ###

    PDF files (.pdf)
    Images (.jpg, .jpeg)

### Project Structure ###

        pdf-image-merger-app/
        │
        ├── app.py              # Main application file
        ├── templates/
        │   └── index.html      # HTML template for the UI
        ├── requirements.txt    # Python dependencies
        └── README.md           # Project documentation

### Contributing ###

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

### License ###

This project is licensed under the MIT License. See the LICENSE file for more information.

### Acknowledgements ###

    Flask - Web framework
    PyPDF2 - PDF handling
    Pillow - Image processing
