import face_recognition
def recognize(actor_file):
    reference = face_recognition.load_image_file(actor_file)
    unknown_image = face_recognition.load_image_file("my_screenshot.jpg")
    
    
    reference_encoding = face_recognition.face_encodings(reference)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    
    results = face_recognition.compare_faces([reference_encoding], unknown_encoding)
    print(results)
if __name__ == "__main__":
    recognize("face.jpg")