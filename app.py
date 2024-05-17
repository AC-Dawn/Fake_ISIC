from flask import Flask, request, jsonify, session, send_from_directory, send_file
import os
import uuid
import datetime
import func


app = Flask(__name__)
app.secret_key = os.urandom(24)  # 使用随机生成的密钥

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


# 设置根 URL 路由，返回 index.html
@app.route('/')
def index():
    return send_file('index.html')


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)


# 文件上传处理路由
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    name = request.form.get('name')
    birth = request.form.get('birth')

    if not name:
        return jsonify({'error': 'Name is required'})
    if not birth:
        return jsonify({'error': 'Birth date is required'})
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # if file and allowed_file(file.filename):
    if file:
        session_id = session.get('id')
        if not session_id:
            session_id = str(uuid.uuid4())
            session['id'] = session_id

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"{session_id}_{timestamp}.png"

        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)

        file.save(upload_path)

        # 在这里进行处理
        func.add_text(name,birth,'','',filename)

        return jsonify({'message': 'success','filename': filename})
    else:
        return jsonify({'error': 'File format not supported'})


if __name__ == '__main__':
    app.run(debug=True)
