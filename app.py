from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import cv2
import numpy as np
from PIL import Image

app = Flask(__name__)

# Đường dẫn thư mục tạm để lưu trữ ảnh tải lên
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def histogram_equalization_cv2(img):
    # Chuyển đổi ảnh sang ảnh xám nếu là ảnh màu
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng Histogram Equalization bằng hàm cv2.equalizeHist
    img_equalized = cv2.equalizeHist(img)

    return img_equalized

def process_image(file_path):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(file_path)

    # Áp dụng Histogram Equalization
    img_equalized = histogram_equalization_cv2(img)

    # Lưu ảnh tạm thời
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp.png')
    cv2.imwrite(temp_path, img_equalized)

    return temp_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        processed_path = process_image(file_path)

        return render_template('index.html', original=file_path, processed=processed_path)

@app.route('/download')
def download_file():
    processed_path = request.args.get('processed_path', '')

    return send_file(processed_path, as_attachment=True)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, port=port)
