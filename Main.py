import face_recognition
import tkinter as tk
from bs4 import BeautifulSoup as bs
#GLobal Variables
actor_success = ""
movie  = "Avengers_Infinity_War"
DEFAULT = ("Times New Roman", 18)
class Movie_frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_instructions = tk.Label(self, font = DEFAULT, 
                                          text = "Enter the IMDB link for the movie you would like to watch").grid(
                                              row="0", column="0")
        self.ent_link = tk.Entry(self, font = DEFAULT, 
                                          text = "Enter the IMDB link for the movie you would like to watch").grid(
                                              row="1", column="0")
        self.btn_submit = tk.Button(self, text = "Submit", bg="green",
                              command = self.imdb_scrape, font=DEFAULT).grid(
                                              row="2", column="0")    
    def get_actors(self):
        actors = imdb_scrape(self.ent_link.get())
    def imdb_scrape(self, website):
        #makes an  html request to the given site
        r = rq.get(website, verify=False)
        html_doc = r.content
        soup = bs(html_doc, 'html.parser')
        actor_table = soup.find_all('td', class_ = 'primary_photo' )
        actors = []
        #print(bs.get_text(actor_table[0].findNextSibling('td')))
        #adds every actor to a list
        for i in range(len(actor_table)):
            #follow a link off of the primary photo and get the images from it
            link = actor_table[i].parent
            print(link)
            actors.append(bs.get_text(actor_table[i].findNextSibling('td')))
        #removes whitespace characters
        for i in range(len(actors)):
            actors[i] = actors[i].strip()
        #print(actors)    
        #get the images of these actors
        return actors    
class Recognize_frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_instructions = tk.Label(self, font = DEFAULT, 
                                          text = "Press the button to recognize the people on screen").grid(
                                              row="0", column="0" , columnspan="2") 
        self.btn_cancel = tk.Button(self, text = "Cancel", bg="red",
                              command = self.raise_movie , font=DEFAULT).grid(
                                              row="1", column="0") 
        self.btn_submit = tk.Button(self, text = "Submit", bg="green",
                              command = self.execute, font=DEFAULT).grid(
                                              row="1", column="1")
        self.lbl_recognized = tk.Label(self, text="Nobody has been recognized yet. Press the button :)",
                                       font=DEFAULT)
        self.lbl_recognized.grid(row="2",column="0" , columnspan="2")
    def raise_movie(self):
        frame_movie.tkraise()    
    def execute(self):
        print('execution start')
        people = ""
        im1 = pyautogui.screenshot('face.jpg')
        print('calling recognize')
        recognized = self.recognize(movie)
        for i in range(len(recognized)):
            people += recognized[i]
            people += " , "
        self.lbl_recognized.config(text = people[:-2])
    def recognize(self, movie):
        actor_success= []
        files = os.listdir("movies/" + movie)
        unknown_image = face_recognition.load_image_file("face.jpg")
        unknown_encoding = face_recognition.face_encodings(unknown_image)
        reference = ""
        reference_encoding = ""
        results = ""
        for file in files:
            reference = face_recognition.load_image_file("movies/" + movie + "/" +file)
            reference_encoding = face_recognition.face_encodings(reference)[0]
            for face_encoding in unknown_encoding:
                results = face_recognition.compare_faces([reference_encoding], face_encoding)
                if results[0] == True:
                    actor_success.append(file[:-4])
        print('recognize completed')
        return actor_success

class Temp_frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_instructions = tk.Label(self, font = DEFAULT, 
                                          text = "")
        self.lbl_instructions.grid(row="0", column="0")    
#tkinter initialization
root = tk.Tk()
root.title("Activity 214")
#The Frame that deals with face recognition stuff
frame_recognize = Recognize_frame()
frame_recognize.grid(row="0", column="0" , sticky="news")
#The Frame to let you choose the movie
frame_movie = Movie_frame()
frame_movie.grid(row="0", column="0", sticky="news")
frame_movie.tkraise()
root.mainloop()