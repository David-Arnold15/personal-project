import pyautogui , os
import face_recognition
from pynput import keyboard
#recognizing the faces themselves
def recognize(movie):
    movie  = "Avengers_Infinity_War"
    files = os.listdir("movies/" + movie)
    for file in files:
        reference = face_recognition.load_image_file("movies/" + movie + "/" +file)
        unknown_image = face_recognition.load_image_file("my_screenshot.jpg")
        
        
        reference_encoding = face_recognition.face_encodings(reference)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    
        results = face_recognition.compare_faces([reference_encoding], unknown_encoding)
    print(results)

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
    ]
def screenshot_process():
    im1 = pyautogui.screenshot('my_screenshot.jpg')
screenshot_process()
current = set()
def execute():
    screenshot_process()
    recognize("face.jpg")
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()