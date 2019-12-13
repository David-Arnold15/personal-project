import  os
#used to recognize faces
import face_recognition
import tkinter as tk
from bs4 import BeautifulSoup as bs
import requests as rq
import pickle
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
        
        self.ent_link = tk.Entry(self, font = DEFAULT,)
        self.ent_link.grid(row="1", column="0")
        
        self.btn_submit = tk.Button(self, text = "Submit", bg="green",
                              command = self.raise_recognize, font=DEFAULT).grid(
                                              row="2", column="0")    
    
    def raise_temp(self):
        actors_characters = self.imdb_scrape(self.ent_link.get())
        actors = actors_characters[0]
        characters = actors_characters[1]
        print(actors)
        print(characters)
        frame_temp.lbl_actors.configure(text = actors )
        frame_temp.tkraise()
    
    def raise_recognize(self):
        frame_recognize.tkraise() 
    
    def imdb_scrape(self, website):
        #makes an  html request to the given site
        r = rq.get(website, verify=False)
        html_doc = r.content
        soup = bs(html_doc, 'html.parser')
        actor_table = soup.find_all('td', class_ = 'primary_photo' )
        actors = []
        characters = []
        #print(bs.get_text(actor_table[0].findNextSibling('td')))
        
        #adds every actor to a list
        for i in range(len(actor_table)):
            actors.append(bs.get_text(actor_table[i].findNextSibling('td')))
            characters.append(bs.get_text(actor_table[i].findNextSibling('td').findNextSibling('td').findNextSibling('td')))
        
        #removes whitespace characters
        for i in range(len(actors)):
            actors[i] = actors[i].strip()
            characters[i] = characters[i].strip()
            #character_remove_whitespace = characters[i].split("/n")
            #characters[i] = character_remove_whitespace[0]
        return [actors , characters]   
    

"""-------------------------------------------------------------------------------------------------------------------------------------"""    

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
        if len(recognized) >=1:
            self.lbl_recognized.config(text = people[:-2])
        else:
            self.lbl_recognized.config(text = "Nobody was recognized, try again")
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


"""-------------------------------------------------------------------------------------------------------------------------------------"""

class Temp_frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.actors = ""
        self.lbl_instructions = tk.Label(self, font = DEFAULT, 
                                         text = "Please find photos for these actors, and ")
        self.lbl_instructions.grid(row="0", column="0")    
        self.lbl_instructions2 = tk.Label(self, font = DEFAULT,
                                          text = "place them in a folder with the name of the movie you are watching: ")
        self.lbl_instructions2.grid(row="1", column="0")    
        self.lbl_actors = tk.Label(self, font = DEFAULT, 
                                         text = "")
        self.lbl_actors.grid(row="2", column="0")            
        


"""-------------------------------------------------------------------------------------------------------------------------------------"""

#tkinter initialization
root = tk.Tk()
root.title("Recognizer")

#The Frame that deals with face recognition stuff
frame_recognize = Recognize_frame()
frame_recognize.grid(row="0", column="0" , sticky="news")

#The Frame to let you choose the movie
frame_movie = Movie_frame()
frame_movie.grid(row="0", column="0", sticky="news")

#Temporary frame with the names of actors in a movie
frame_temp = Temp_frame()
frame_temp.grid(row="0", column="0", sticky="news")

#creating the mainloop
frame_movie.tkraise()
root.mainloop()