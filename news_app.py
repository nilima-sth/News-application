import io
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
import webbrowser


class NewsApp:
    def __init__(self):
        #fetch data from api
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=ccf9bc74948442a08bb94189049c3d82').json()
        #loading gui from tkinter
        self.load_gui()
        self.load_news_item(0)
        self.root.mainloop()
    def load_gui(self):
        self.root=Tk()
        self.root.geometry("500x700")
        self.root.resizable(0,0)
        self.root.configure(background='#CAE0BC')
        self.root.title('News application')
    def load_news_item(self,index):
        #clear the current news for next news
        self.clear()
        #print the next news item
        '''Photp/Heading/details'''

        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()  # binary data is being read here
            im = Image.open(io.BytesIO(raw_data)).resize((450, 350))
            self.photo = ImageTk.PhotoImage(im)
            label = Label(self.root, image=self.photo)
            label.pack()
        except:
            img_url =  'https://images.app.goo.gl/TrdWyfSiYHxCqZj99'
            raw_data = urlopen(img_url).read()  # binary data is being read here
            im = Image.open(io.BytesIO(raw_data)).resize((450, 350))
            self.photo = ImageTk.PhotoImage(im)
            label = Label(self.root, image=self.photo)
            label.pack()

        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='#CAE0BC',fg='black',justify='center',wraplength=400)
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',14,'bold'))

        description_label=Label(self.root,text="Description",bg='white',fg='black')
        description_label.pack(pady=(5,5))
        description_label.config(font=('verdana',12))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='#CAE0BC', fg='black',
                         wraplength=500)
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg='white')
        frame.pack(expand=True, fill=BOTH)

        if index != 0:
            prev=Button(frame,text="Previous",width=19,height=5,command=lambda : self.load_news_item((index-1)))
            prev.pack(side=LEFT)

        Read = Button(frame, text="Read more", width=19, height=5,command=lambda : self.open_link(self.data['articles'][index]['url']))
        Read.pack(padx=(30,20),side=LEFT)
        if index != len(self.data['articles'])-1:
            next = Button(frame, text="Next", width=19, height=5, command=lambda : self.load_news_item((index+1)))
            next.pack(side=RIGHT)

    def clear(self):
        for i in self.root.pack_slaves(): #pack_slaves are the items inside the geometry
            i.destroy()
    def open_link(self,url):
        webbrowser.open(url)

obj=NewsApp()
