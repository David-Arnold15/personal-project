#used to take a screenshot
import pyautogui 
#file management
import os
#used to recognize faces
import face_recognition
#builds the GUI
import tkinter as tk
#used to process the HTML file
from bs4 import BeautifulSoup as bs
#requests the HTMl file from a website
import requests as rq
#used to store variables as a data file
import pickle
#GLobal Variables
actor_success = ""
movie  = "Avengers_Infinity_War"
DEFAULT = ("Times New Roman", 18)


"""this program allows the user to recognize famous faces in movies, with the names of the characters they play by pulling a list of
actors off of IMDB"""
#Data classes
class Movies(object):
    def __init__(self):
        self.actor_dict = {}
        self.actors = []
        self.movie_name = "Avengers_Infinity_War"
        #temporary dictionary. Final version will use pickle to pull full list
        try:
            self.pickled_dict = open("movie_dict.p", "rb")
            self.movie_dict = pickle.load(self.pickled_dict)
            self.pickled_dict.close()
            print("option 1")
        except:
            self.pickled_dict = open("movie_dict.p", "wb")
            self.movie_dict = {"Avengers_Infinity_War" : {"Chris Hemsworth":"Thor" , "Robert Downey JR":"Iron Man"}}
            pickle.dump(self.movie_dict, self.pickled_dict)
            self.pickled_dict.close()
            print("option 2")
        
    def scraper(self, website):
        actors_characters = self.imdb_scrape(website)
        self.actors = actors_characters[0]
        print(len(self.actors)/5)
        characters = actors_characters[1]
        
        for i in range(len(characters)):
            self.actor_dict[self.actors[i]] = characters[i]     
        
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
"""--------------------------------------------------------------------------------------------------------------------------------------"""
#Frame Classes
class Movie_frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_instructions = tk.Label(self, font = DEFAULT, 
                                          text = "Enter the IMDB link for the movie you would like to watch").grid(
                                              row="0", column="0" , columnspan = "2")
        
        #This is where the user enters a link to the movie they wish to watch
        self.ent_link = tk.Entry(self, font = DEFAULT,)
        self.ent_link.grid(row="1", column="0" , columnspan = "2")
        
        #the buttons that quit or submit
        self.btn_quit = tk.Button(self, text = "quit", bg="red",
                              command = self.quit, font=DEFAULT).grid(
                                              row="2", column="0")    
        
        self.btn_submit = tk.Button(self, text = "Submit", bg="green",
                              command = self.raise_movie_name_frame, font=DEFAULT).grid(
                                              row="2", column="1" )        
    def quit(self):
        root.destroy()
    def raise_movie_name_frame(self):
        movies.scraper(self.ent_link.get())
        frame_movie_name.tkraise()
    def raise_recognize(self):
        frame_recognize.tkraise() 
    
       
    

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
        self.btn_exit = tk.Button(self, text = "Exit", bg="red",
                                  command = self.exit ,font = DEFAULT).grid(
                                      row="3", column="0", columnspan = "2")        
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
        files = os.listdir("movies/" + movies.movie_name)
        unknown_image = face_recognition.load_image_file("face.jpg")
        unknown_encoding = face_recognition.face_encodings(unknown_image)
        reference = ""
        reference_encoding = ""
        results = ""
        
        for file in files:
            reference = face_recognition.load_image_file("movies/" + movies.movie_name + "/" +file)
            reference_encoding = face_recognition.face_encodings(reference)[0]
            
            for face_encoding in unknown_encoding:
                results = face_recognition.compare_faces([reference_encoding], face_encoding)
                
                if results[0] == True:
                    actor_success.append(file[:-4])
        print('recognize completed')
        return actor_success
    def exit(self):
        movies_file = open("./movies/movie_dict.p", "wb")
        pickle.dump(movies.movie_dict, movies_file)
        movies_file.close()
        root.destroy()    


"""-------------------------------------------------------------------------------------------------------------------------------------"""
class Movie_name_frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        #tells the user what to do
        self.lbl_instructions = tk.Label(self, font = DEFAULT, 
                                         text = "What is the name of the movie you would like to watch? Please exclude special characters")
        self.lbl_instructions.grid(row="0", column="0" , columnspan = "2")
        
        #field for the user to enter in the name of the movie
        self.ent_title = tk.Entry(self, font = DEFAULT,)
        self.ent_title.grid(row="1", column="0" , columnspan = "2")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", bg="Red",
                              command = self.raise_movie_frame, font=DEFAULT).grid(
                                              row="2", column="0")
        self.btn_submit = tk.Button(self, text = "Submit", bg="green",
                              command = self.raise_movie_frame, font=DEFAULT).grid(
                                              row="2", column="1")
    def raise_movie_frame(self):
        movie = self.ent_title.get()
        movies.movie_name = movie
        if movie in movies.movie_dict.keys():
            frame_recognize.tkraise()
        else:
            frame_movie.tkraise()
            
    def raise_temp(self):
        #print(actors)
        #print(characters)
        
        #changes the text on the temp frame to the names of the actors
        frame_temp.lbl_actors1.configure(text = movies.actors[0:5] )
        frame_temp.lbl_actors2.configure(text = movies.actors[5:10] )
        frame_temp.lbl_actors3.configure(text = movies.actors[10:15] )
        frame_temp.tkraise()
    

class Temp_frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.actors = ""
        self.lbl_instructions = tk.Label(self, font = DEFAULT, 
                                         text = "Please find photos for these actors, and ")
        self.lbl_instructions.grid(row="0", column="0" , columnspan = "2")
        
        self.lbl_instructions2 = tk.Label(self, font = DEFAULT,
                                          text = "place them in a folder with the name of the movie you are watching: ")
        self.lbl_instructions2.grid(row="1", column="0" , columnspan = "2")    
        
        #labels holding the names of the actors
        self.lbl_actors1 = tk.Label(self, font = DEFAULT, 
                                         text = "")
        self.lbl_actors1.grid(row="2", column="0" , columnspan = "2")
       
        self.lbl_actors2 = tk.Label(self, font = DEFAULT, 
                                         text = "")
        self.lbl_actors2.grid(row="3", column="0" , columnspan = "2")
       
        self.lbl_actors3 = tk.Label(self, font = DEFAULT, 
                                         text = "")
        self.lbl_actors3.grid(row="4", column="0" , columnspan = "2")        
        
        #these are the buttons to cancel or submit
        self.btn_cancel = tk.Button(self, text = "Cancel", bg="Red",
                              command = self.test, font=DEFAULT).grid(
                                              row="5", column="0") 
        self.btn_submit = tk.Button(self, text = "Submit", bg="green",
                              command = self.raise_recognize, font=DEFAULT).grid(
                                              row="5", column="1")        
    def test(self):
        pass

    def raise_recognize(self):
        frame_recognize.tkraise()
 
"""-------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------"""
#dataclass initialization
movies = Movies()
"""initializing tkinter Windows
This is where the magic happens"""



#tkinter initialization
root = tk.Tk()
root.title("Recognizer")

#The Frame that deals with face recognition stuff
frame_recognize = Recognize_frame()
frame_recognize.grid(row="0", column="0" , sticky="news")

#The Frame to let you choose the movie
frame_movie = Movie_frame()
frame_movie.grid(row="0", column="0", sticky="news")

#The frame to add the name of a movie to a folder name
frame_movie_name = Movie_name_frame()
frame_movie_name.grid(row="0", column="0", sticky="news")

#Temporary frame with the names of actors in a movie
frame_temp = Temp_frame()
frame_temp.grid(row="0", column="0", sticky="news")

#creating the mainloop
frame_movie_name.tkraise()
root.mainloop()     