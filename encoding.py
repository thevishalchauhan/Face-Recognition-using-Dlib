import face_recognition
import pickle

# Load a sample picture and learn how to recognize it.
vishal_image = face_recognition.load_image_file("Vishal.jpg")
vishal_face_encoding = face_recognition.face_encodings(vishal_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    vishal_face_encoding
]
known_face_names = [
    "Vishal"
]

with open("face_encoding","wb") as f:
    pickle.dump((known_face_encodings,known_face_names),f)
