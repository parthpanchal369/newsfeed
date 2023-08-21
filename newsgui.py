import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image


class NewsApp:

    def __init__(self):

        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey"
                            "=eb617852263445d8a282507ac0c0fa5a").json()

        print(self.data)
        self.load_gui()

        self.load_news_items(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.resizable(0,0)
        self.root.title('Parth News APP')
        self.root.configure(background='blue')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_items(self, index):

        self.clear()

# Image part
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 200))
            photo = ImageTk.PhotoImage(im)

        except:
            img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/' \
                      'No_image_available.svg/300px-No_image_available.svg.png'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 200))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=photo)
        label.pack()

# Heading code
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='red', fg='white',
                        wraplength=350, justify='center')
        heading.pack(pady=(20, 30))
        heading.config(font=('verdana'))

#Details code
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black',
                            fg='white',wraplength=350, justify='center')

        details.pack(pady=(2, 30))
        details.config(font=('verdana'))


        frame = Frame(self.root, bg='blue')
        frame.pack(expand=True, fill=BOTH)

        if index != 0:
            prev = Button(frame, text='prev', width=23, height=3,command=lambda :self.load_news_items(
                index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=22, height=3,command=lambda :self.open_link(
            self.data['articles'][index]['url']))

        read.pack(side=LEFT)
        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=23, height=3,command= lambda :self.load_news_items(
                index+1))
            next.pack(side=LEFT)


        self.root.mainloop()


    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()
