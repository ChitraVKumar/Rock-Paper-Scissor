import random
from random import randint
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()  # creating instance of the class Tk
style = ttk.Style()
root.title("Rock,Paper,Scissor")  # Setting title for the window root
root.iconbitmap("D:\RockPaperScissors\RockPaperScissor\RPS.ico")  # setting the icon image
app_width = 1040
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2)-(app_width/2)
y = (screen_height/2)-(app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# change bg color to black
root.config(bg="#2D2327")

# Opening the images in order to resize them
Rock = Image.open("Images\Rock.png")  # size = 300x250
Paper = Image.open("Images\Paper.png")  # size = 915x1024
Scissor = Image.open("Images\scissor.png")  # size = 800x659
Rock_comp = Image.open("Images\Rock_comp.png")  # size = 181x179
Paper_comp = Image.open("Images\Paper_comp.png")  # size = 180x189
Scissor_comp = Image.open("Images\scissor_comp.png")  # size = 178x180

# Resizing the image and preventing aliases
resized_rock = Rock.resize((150, 130), Image.ANTIALIAS)
resized_paper = Paper.resize((150, 130), Image.ANTIALIAS)
resized_scissor = Scissor.resize((150, 130), Image.ANTIALIAS)
resized_rk = Rock_comp.resize((150, 130), Image.ANTIALIAS)
resized_pap = Paper_comp.resize((150, 130), Image.ANTIALIAS)
resized_sci = Scissor_comp.resize((150, 130), Image.ANTIALIAS)

# Moves Images
new_rock = ImageTk.PhotoImage(resized_rock)
new_paper = ImageTk.PhotoImage(resized_paper)
new_scissor = ImageTk.PhotoImage(resized_scissor)
new_rock_Clone = ImageTk.PhotoImage(resized_rk)
new_paper_Clone = ImageTk.PhotoImage(resized_pap)
new_scissor_Clone = ImageTk.PhotoImage(resized_sci)

# Adding all the images to a list
player_image_list = [new_rock, new_paper, new_scissor]
clone_image_list = [new_rock_Clone, new_paper_Clone, new_scissor_Clone]

# Picking a random integer
pick_num = random.randint(0, 2)
moves = ["Rock", "Paper", "Scissor"]

# USer image label # Clone image label
player_image_label = Label(root, image=player_image_list[pick_num], bd=0, bg="#E072A4")
player_image_label.grid(row=1, column=0, padx=20, pady=20)
clone_image_label = Label(root, image=random.choice(clone_image_list), bd=0, bg="#E072A4")
clone_image_label.grid(row=1, column=4)

# Player and Clone scores
score_player_label = Label(root, text=0, font=200, bg="#2D2327",
                           fg="#f4e900")
score_player_label.grid(row=1, column=1, padx=15, pady=15)
score_clone_label = Label(root, text=0, font=200, bg="#2D2327",
                          fg="#f4e900")
score_clone_label.grid(row=1, column=3, padx=15, pady=15)

# Text above the buttons
select_text = Label(root, text="Pick Your Moves!", bg="#2D2327", fg="white", font=("Arial Bold", 16)).grid(row=5,
                                                                                                           column=2)

# Buttons to select the moves
Rock = Button(root, text="Rock", width=20, height=2, bg="#595cff", fg="black",
              command=lambda: all_moves("Rock")).grid(row=5, column=1, padx=40, pady=40)
Paper = Button(root, text="Paper", width=20, height=2, bg="#ff0f7b", fg="black",
               command=lambda: all_moves("Paper")).grid(row=6, column=2, padx=20, pady=20)
Scissor = Button(root, text="Scissor", width=20, height=2, bg="#59d102", fg="black",
                 command=lambda: all_moves("Scissor")).grid(row=5, column=3, padx=40,
                                                            pady=40)

# Player and Clone label
player_label = Label(root, text="PLAYER", bg="#2D2327", fg="#f4e900", font=("Arial Bold", 22)).grid(row=0, column=0,
                                                                                                    padx=20, pady=20)
clone_label = Label(root, text="COMPUTER", bg="#2D2327", fg="#f4e900", font=("Arial Bold", 22)).grid(row=0, column=4,
                                                                                                     padx=20, pady=20)

# messages on win, lose or draw
message = Label(root, font=50, bg="#2D2327", fg="#f4e900")
message.grid(row=1, column=2)


def all_moves(player_moves):
    # For clone
    clone_moves = moves[randint(0, 2)]
    if clone_moves == "Rock":
        clone_image_label.config(image=new_rock_Clone)
    elif clone_moves == "Paper":
        clone_image_label.config(image=new_paper_Clone)
    else:
        clone_image_label.config(image=new_scissor_Clone)

    # For player
    if player_moves == "Rock":
        player_image_label.config(image=new_rock)
    elif player_moves == "Paper":
        player_image_label.config(image=new_paper)
    else:
        player_image_label.config(image=new_scissor)

    play(player_moves, clone_moves)


# function definition for winner:
def play(a, b):  # a and b represent player as user and opponent as computer/clone
    if a == b:
        infor("It's a Tie!")
        player_score()
        clone_score()

    # paper beats rock, rock beat scissor, scissor beats paper
    elif (a == 'Paper' and b == 'Rock') or (a == 'Rock' and b == 'Scissor') or \
            (a == 'Scissor' and b == 'Paper'):
        infor("You Win!")
        player_score()
    else:
        infor("You Lose!!")
        clone_score()


# function definition for messages to pop
def infor(text):
    message.config(text=text)


def player_score():
    p_score = int(score_player_label["text"])
    p_score += 1
    score_player_label["text"] = str(p_score)


def clone_score():
    c_score = int(score_clone_label["text"])
    c_score += 1
    score_clone_label["text"] = str(c_score)


root.mainloop()
