import customtkinter
import tkinter as tk
from PIL import Image

BOLD_FONT = ("Arial", 12, "bold")

class Ranking():

    def __init__(self, database):
        self.database = database
        self.width = 800
        self.height = 600
        self.screen = customtkinter.CTk()
        self.screen.title("Ranking")
        customtkinter.set_appearance_mode("dark")
        self.screen.resizable(False, False)

        # Centers the window
        screen_width = self.screen.winfo_screenwidth()
        screen_height = self.screen.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) -  ( self.height / 2)

        self.screen.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))


        self.email_labels = []
        self.score_labels = []
    
    def add_email_in_label(self):
         for i, email in enumerate(self.database.get_email_ranking()):
                label = tk.Label(self.screen, text=email, font=BOLD_FONT, width=0, height=0, bg="#b4b4b4")
                label.place(x=250, y=60*i+155)
                self.email_labels.append(label)
    
    def add_score_in_label(self):
         for i, score in enumerate(self.database.get_score_ranking()):
                label = tk.Label(self.screen, text=score, font=BOLD_FONT, width=0, height=0, bg="#b4b4b4")
                label.place(x=625, y=60*i+155)
                self.score_labels.append(label)

    def create_ranking_screen(self):
        ranking_bg = customtkinter.CTkImage(Image.open("resources/ranking_bg.png"), size=(800, 600))
        main_label = customtkinter.CTkLabel(self.screen, text="", image=ranking_bg)
        main_label.place(x=0, y=0)
        self.add_email_in_label()
        self.add_score_in_label()

        self.screen.mainloop()