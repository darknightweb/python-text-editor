import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="pick a color or choose you like one")
    text_area.config(fg=color[1])
    
    
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    windows.title("untitle")
    text_area.delete(1.0, END)


def open_file():
    file= askopenfilename(defaultextension=".txt", 
                         filetypes=[("All Files", "*.*"), 
                         ("text documents", "*.txt")])

    try:
        windows.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())
    
    except Exception:
        print("file is not opening")
    
    finally:
        file.close()



def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitle.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", 
                                        "*.*"), ("text Documents", 
                                        "*.txt")])
    if file is None:
        return
    
    else:
        try:
            windows.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))
        except Exception:
            print("cant save the file")
            
        finally:
            file.close()
    
    
def cut():
     text_area.event_generate("<<Cut>>")



def copy():
     text_area.event_generate("<<Copy>>")

    

def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this program", "The programe written in python by subhash maurya , its a simple programe of text editor.")


def quit():
    windows.destroy()


windows = Tk()

windows.title("simple text editor programs")

#screen resolution setting

file = None
windows_width = 500
windows_height = 500

screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()


x = int((screen_width / 2) - (screen_width / 2))
y = int((screen_height / 2) - (screen_height / 2))
 
windows.geometry("{}x{}+{}+{}".format(windows_width,windows_height, x, y))

font_name = StringVar(windows)
font_name.set("Arial")

font_size = StringVar(windows)
font_size.set("25")

#text area

text_area = Text(windows, font=(font_name.get(),font_size.get()))

#scroll bar

scroll_bar = Scrollbar(text_area)
windows.grid_rowconfigure(0, weight=1)
windows.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)


#adding button in loewr parts

frame = Frame(windows)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box  =Spinbox(frame, from_=1, to=100, textvariable=font_size,command=change_font)
size_box.grid(row=0, column=2)


scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand = scroll_bar.set)


#setting main menubars

menu_bar = Menu(windows)
windows.config(menu = menu_bar)


file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="new", command= new_file)
file_menu.add_command(label="open", command= open_file)
file_menu.add_command(label="save", command = save_file)
file_menu.add_separator()
file_menu.add_command(label="exit", command= quit)


edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="cut", command=cut)
edit_menu.add_command(label="copy", command=copy)
edit_menu.add_command(label="paste", command =paste)


help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu = help_menu)
help_menu.add_command(label="About", command=about)


windows.mainloop()
