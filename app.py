from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download_audio', methods=['POST'])
def download_audio():
    data = request.get_json()
    video_id = data.get('video_id')
    if not video_id:
        return jsonify({"error": "No video ID provided"}), 400
    
    # Download and processing logic here
    return jsonify({"message": "Audio downloaded"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
