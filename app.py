from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    
    return text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

