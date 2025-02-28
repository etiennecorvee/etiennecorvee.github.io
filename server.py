from flask import Flask, send_from_directory
from flask import Flask, render_template

app = Flask(__name__, static_folder="static")
# app = Flask(__name__)

@app.route("/")
def serve_index():
    # return send_from_directory("templates", "index-old.html")
    return send_from_directory(".", "index.html")
    # return render_template("index.html")

@app.route("/static/videos/<path:filename>")
def serve_video(filename):
    return send_from_directory("static/videos", filename, mimetype="video/mp4")  # Ensure correct MIME type

# @app.route("/<path:filename>")
# def serve_static(filename):
#     return send_from_directory(".", filename, mimetype=get_mime_type(filename))

# def get_mime_type(filename):
#     if filename.endswith(".mp4"):
#         return "video/mp4"
#     elif filename.endswith(".webm"):
#         return "video/webm"
#     elif filename.endswith(".ogg"):
#         return "video/ogg"
#     return None  # Let Flask handle other files normally

if __name__ == "__main__":
    app.run(debug=True)
