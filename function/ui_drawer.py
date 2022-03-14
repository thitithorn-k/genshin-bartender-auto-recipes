import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from function.game_screen import get_screen
import function.drink as drink
import cv2

drink_names = [
    'Athenaeum',
    'Caramel Pinecone',
    'Foamy Reef',
    'Golden Eden',
    'Moonlit Alley',
    'Night of Swirling Stars',
    'Boreal Watch',
    'Brightcrown',
    'Laughter And Cheer',
    'Love Poem',
    'Misty Garden',
    'Scholar\'s Afternoon',
    'Tart Brilliance',
    'Barbatos\' Boon',
    'Birch Sap',
    'Dawning Dew',
    'Gray Valley Sunset',
    'Snow-Covered Kiss',
    'Sweet Cider Lake',
    'Dusk',
    'Stroke Of Night'
]

recipe_images = []

for i in range(9):
    img = Image.open(f'resources/recipes/{i}.jpg')
    recipe_images.append(img)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Genshin Bartender Auto Recipes')
        self.attributes('-topmost', True)
        self.resizable(0, 0)
        self.geometry('200x310')
        self['bg'] = '#f0f0f0'

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='#f0f0f0',
            foreground='black')

        # head
        self.head = ttk.Label(
            self,
            text='Game window found' if get_screen(True) else 'Game window not found',
            font=('', 12))
        self.head.pack()

        self.last_drink = -99

        self.drink_name = ttk.Label(
            self,
            text='',
            font=('', 10))
        self.drink_name.pack()

        self.recipe_img_1 = tk.Label(self, image=None)
        self.recipe_img_1.pack()
        self.recipe_amount_1 = ttk.Label(
            self,
            text='',
            font=('', 10))
        self.recipe_amount_1.pack()

        self.recipe_img_2 = tk.Label(self, image=None)
        self.recipe_img_2.pack()
        self.recipe_amount_2 = ttk.Label(
            self,
            text='',
            font=('', 10))
        self.recipe_amount_2.pack()

        self.recipe_img_3 = tk.Label(self, image=None)
        self.recipe_img_3.pack()
        self.recipe_amount_3 = ttk.Label(
            self,
            text='',
            font=('', 10))
        self.recipe_amount_3.pack()

        # schedule an update every 1 second
        self.head.after(1000, self.update)

    def update(self):
        if not get_screen(True):
            self.head.configure(text='Game window not found')
        else:
            self.head.configure(text='Game window found')
            recipes = drink.get_recipe()
            if recipes is not -1:
                if self.last_drink is not recipes[0]:
                    self.last_drink = recipes[0]
                    self.drink_name.configure(text='Order: ' + drink_names[recipes[0]])

                    if len(recipes[1]) >= 1:
                        imgtk1 = ImageTk.PhotoImage(image=recipe_images[recipes[1][0][0]])
                        amount_1 = recipes[1][0][1]
                    else:
                        imgtk1 = None
                        amount_1 = ''
                    self.recipe_img_1.configure(image=imgtk1)
                    self.recipe_img_1.photo = imgtk1
                    self.recipe_amount_1.configure(text=amount_1)

                    if len(recipes[1]) >= 2:
                        imgtk2 = ImageTk.PhotoImage(image=recipe_images[recipes[1][1][0]])
                        amount_2 = recipes[1][1][1]
                    else:
                        imgtk2 = None
                        amount_2 = ''
                    self.recipe_img_2.configure(image=imgtk2)
                    self.recipe_img_2.photo = imgtk2
                    self.recipe_amount_2.configure(text=amount_2)

                    if len(recipes[1]) >= 3:
                        imgtk3 = ImageTk.PhotoImage(image=recipe_images[recipes[1][2][0]])
                        amount_3 = recipes[1][2][1]
                    else:
                        imgtk3 = None
                        amount_3 = ''
                    self.recipe_img_3.configure(image=imgtk3)
                    self.recipe_img_3.photo = imgtk3
                    self.recipe_amount_3.configure(text=amount_3)
            else:
                self.last_drink = -99
                self.drink_name.configure(text='Order not found')
                self.recipe_img_1.configure(image=None)
                self.recipe_img_2.configure(image=None)
                self.recipe_img_3.configure(image=None)
                self.recipe_img_1.photo = None
                self.recipe_img_2.photo = None
                self.recipe_img_3.photo = None
                self.recipe_amount_1.configure(text='')
                self.recipe_amount_2.configure(text='')
                self.recipe_amount_3.configure(text='')


        # schedule another timer
        self.head.after(1000, self.update)

