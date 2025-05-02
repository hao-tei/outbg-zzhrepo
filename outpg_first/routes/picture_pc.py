from outpg_first.routes import app
import os
from flask import render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'ssets/img'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'message': '没有文件'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'message': '未选择文件'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': f'文件已上传: {filename}'})
    else:
        return jsonify({'message': '文件类型不被允许'}), 400



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
