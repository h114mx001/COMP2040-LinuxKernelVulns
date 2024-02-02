from flask import Flask, render_template
from flask import request, send_file
from PIL import Image, ImageDraw, ImageFont
import random
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/meme", methods=['POST'])
def generate_meme():
    # Get the text from the form submission
    text = request.form.get('inputText')

    subprocess.check_output(f"python3 ./image_writer.py -t {text}", shell=True)
    # Return the new image
    return send_file('meme_with_text.jpg', mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug = False, port=5000)