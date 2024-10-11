from flask import Flask, request, render_template, jsonify
from flask_cors import CORS  # เพิ่มการนำเข้า
from emotion_model import predict_emotion
import requests

app = Flask(__name__)
CORS(app)  # เพิ่มบรรทัดนี้เพื่ออนุญาต CORS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_song', methods=['POST'])
def search_song():
    data = request.get_json()
    user_input = data.get('user_input')

    if not user_input:
        return jsonify({"error": "กรุณาใส่ข้อความที่ต้องการ"}), 400

    # ตรวจจับอารมณ์จากข้อความที่ผู้ใช้พิมพ์
    emotion = predict_emotion(user_input)

    # ใช้ Client Access Token เป็น API Key
    api_key = "Kny_lrpNvJp60Azp_87xYJa-TnXkl35nfIh6weHBE3n8oHK7pSWO4Q7zWiVlj_Td"
    base_url = "https://api.genius.com/search"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        'q': emotion  # ค้นหาเพลงจากอารมณ์ที่ตรวจจับได้
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json()
        songs = result['response']['hits']
        
        if songs:
            return jsonify(songs), 200
        else:
            return jsonify({"error": "ไม่พบเพลงที่ตรงกับอารมณ์"}), 404
    else:
        return jsonify({"error": "เกิดข้อผิดพลาดในการค้นหา"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
