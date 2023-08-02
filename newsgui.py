import requests
from tkinter import *

class NewsApp:

    def __init__(self):

        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey"
                            "=eb617852263445d8a282507ac0c0fa5a").json()

        # print(self.data)
        self.load_gui()
        self.root.mainloop()


    def load_gui(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.configure(background='blue')


obj = NewsApp()