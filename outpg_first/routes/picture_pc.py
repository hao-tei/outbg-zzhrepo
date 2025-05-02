from outpg_first.routes import app
import os
from flask import render_template, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
UPLOAD_FOLDER = os.path.join(app.static_folder, 'img')
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
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_path)

        # 模拟“处理”图片：复制并改名
        processed_filename = filename.rsplit('.', 1)[0] + '_processed.' + filename.rsplit('.', 1)[1]
        processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)

        # 模拟处理操作，这里直接复制
        image = Image.open(original_path)
        image.save(processed_path)

        # 返回图片的访问 URL
        image_url = url_for('uploaded_file', filename=processed_filename, _external=True)
        return jsonify({'message': '处理成功', 'image_url': image_url})
    else:
        return jsonify({'message': '文件类型不被允许'}), 400

# 添加新路由用于返回上传文件
@app.route('/assets/img/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
