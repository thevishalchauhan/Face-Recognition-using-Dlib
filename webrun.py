from flask import Flask,render_template,request
from glob import glob
import face_recognition
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("WebCamBrowser.html")

@app.route('/send/',methods=['POST'])
def process():
    image_name = glob('*.jpeg')[0]
    person_name = image_name[:-5]
    image_load = face_recognition.load_image_file(image_name)
    face_encoding = face_recognition.face_encodings(image_load)[0]
    # Create arrays of known face encodings and their names
    known_face_encodings = [
        face_encoding
    ]
    known_face_names = [
        person_name
    ]
    with open("face_encoding","ab") as f:
        pickle.dump((known_face_encodings,known_face_names),f)
    return render_template("WebCamBrowser.html")

if __name__ == "__main__":
    app.run(debug = True)
