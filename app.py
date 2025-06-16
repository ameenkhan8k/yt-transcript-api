from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/transcript")
def transcript():
    video_id = request.args.get("video_id")

    if not video_id:
        return jsonify({"error": "Missing or invalid video_id"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcript)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
