from tkinter import *
from PIL import ImageTk, Image
import random
import tkinter.messagebox as tmsg
import os

app = Tk()
count = 0
comp = random.randint(1, 101)  # Initialize the random number


def generate():
    """Generate a new random number and reset the count."""
    global comp, count
    comp = random.randint(1, 101)
    count = 0  # Reset count when generating a new number


def basic():
    """Setup the main game window and UI components."""
    global app

    app.title("Number Guessing Game")
    app.geometry("500x500")
    app.resizable(False, False)

    # Load and set the icon
    if os.path.exists("guess.png"):
        photo = PhotoImage(file="guess.png")
        app.iconphoto(False, photo)

    Label(app, text='Number Guessing Game', font="Helvetica 18 bold",
          bg='black', fg='tomato', padx=170).pack()

    # Handle missing score file
    if not os.path.exists("score.txt"):
        with open("score.txt", "w") as f:
            f.write("0")

    with open('score.txt', 'r') as f:
        hg = f.read()

    Label(app, text=f'Previous score: {hg}', font='lucida 8 bold').pack(anchor=E, padx=25, pady=5)

    # Footer
    Label(app, text='Developed by SURBHIDEEP', font="Helvetica 8 bold",
          bg='black', fg='tomato', padx=153).pack(side=BOTTOM)

    # Menu
    mymenu = Menu(app)
    file_menu = Menu(mymenu, tearoff=0)
    mymenu.add_cascade(label='Start', menu=file_menu)
    mymenu.add_cascade(label='Restart', command=restart)
    mymenu.add_command(label='About', command=call1)
    mymenu.add_command(label='Quit', command=app.quit)
    app.config(menu=mymenu)

    generate()


def result():
    """Check user's guess and provide feedback."""
    global count
    number = userv.get()

    if number == '':
        tmsg.showerror('Error', "Please enter a value")
        return

    try:
        n = int(number)
    except ValueError:
        tmsg.showerror('Error', "Invalid input! Please enter a number.")
        return

    count += 1
    if count >= 10:
        tmsg.showinfo('Game Over', f'You lost the game! The number was {comp}')
        restart()
    elif comp == n:
        score = 11 - count
        tmsg.showinfo('Win', f'You guessed the right number!\nYour score: {score}')
        show.config(text='Win!', fg='green')

        with open('score.txt', 'w') as f:
            f.write(str(score))

        generate()
        tmsg.showinfo('Next Number', 'Click OK to guess another number')
    elif comp > n:
        show.config(text='Select a greater number', fg='red')
    else:
        show.config(text='Select a smaller number', fg='red')


def restart():
    """Restart the game by generating a new number."""
    tmsg.showinfo('Reset', "Game reset!")
    generate()


def call1():
    """Show information about the game."""
    str1 = 'This game is developed by SURBHIDEEP\n\nCopyright @2025'
    tmsg.showinfo('About', str1)


# Initialize game window
basic()

# Input Field
userv = StringVar()
user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT,
             borderwidth=2, font='Helvetica 18 bold')
user.pack(pady=10)

# Load the game image
image_path = os.path.join(os.path.dirname(__file__), "guess.png")
if os.path.exists(image_path):
    img = ImageTk.PhotoImage(Image.open(image_path))
    Label(app, image=img).pack(pady=30)
else:
    print("Error: guess.png not found!")


# Load the button image (bt.jpeg)
if os.path.exists('bt.jpeg'):
    i = Image.open('bt.jpeg')
    resized_image = i.resize((150, 50), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    submit = Button(app, image=new_image, command=result, relief=FLAT)
else:
    print("Warning: bt.jpeg not found! Using default button.")
    submit = Button(app, text="Submit", command=result, font='Helvetica 18 bold', relief=FLAT)

submit.pack(pady=10)

# Label to show hints
show = Label(app, text='', font='Helvetica 12 bold')
show.pack(pady=10)

app.mainloop()
