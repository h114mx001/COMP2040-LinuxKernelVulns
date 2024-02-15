from flask import Flask, render_template
from flask import request, send_file
import os 

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/meme", methods=['POST'])
def generate_meme():
    # Get the text from the form submission
    text = request.form.get('text')
    # print(text)
    os.system(f"python3 ./image_writer.py {text}")    
    # subprocess.check_output(f"python3 ./image_writer.py -t {text}", shell=True)
    # Return the new image
    return send_file('meme_with_text.png', mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug = False, port=5000, host="0.0.0.0")