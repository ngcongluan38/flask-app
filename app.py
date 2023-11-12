from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file:
        image = Image.open(file)
        bw_image = image.convert('L')

        result = io.BytesIO()
        bw_image.save(result, format="PNG")
        result.seek(0)

        return send_file(result, mimetype='image/png', as_attachment=True, download_name='bw_image.png')

if __name__ == '__main__':
    app.run(debug=True)
