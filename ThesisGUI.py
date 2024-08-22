from tkinter import *
from tkinter import filedialog

# Initialize Tk Class
simu = Tk()

# App Simulator Title
simu.title("Thesis Simulation")

# Class
# not used yet
class Main(Tk):
    def __init__(self):
        super().__init__()
# simu = Main()

# Functions
# Button Interaction
def toggle_About(e):
    global show
    if show:
        aboutWindow.place(relx=0.99, rely=0.15, anchor=NE)
    else:
        aboutWindow.place_forget()
    show = not show
# ~ ~ ~
def toggle_Summarizer():
    # The delay of button animation is intended by using .after() method
    # remove results.after() method if needed for faster testing, or turn the seconds(500ms) lower
    summarizer = Button(simu, text='Summarize', borderwidth=2, state='normal', background='antiquewhite', width=12, height=2, activebackground='antiquewhite4', activeforeground="white", font=('Calibri Bold', 9), cursor='hand2', command=lambda: results.after(500,toggle_Results()))
    # command=toggle_Results() <-- no results.after() method
    # summarizer.bind('<Button-1>', toggle_Results)
    summarizer.place(relx=0.78, rely=0.05, anchor=NE)
# ~ ~ ~
def toggle_Results():
    results = Button(simu, text='Results', borderwidth=2, state='normal', background='antiquewhite', width=12, height=2, activebackground='antiquewhite4', activeforeground="white", font=('Calibri Bold', 9), cursor='hand2', command=lambda: toggle_tabResults())
    # results.bind('<Button-1>', toggle_tabResults)
    results.place(relx=0.88, rely=0.05, anchor=NE)
# ~ ~ ~
def toggle_tabResults():
    global result
    if result:
        resultsWindow.place(anchor=SE, relx=0.98, rely=0.9)
    else:
        resultsWindow.place_forget()
    result = not result
    
# file = askopenfilename()
# this is not a working function currently
def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt"),("PDF Files", "*.pdf"),("DOCX Files", "*.docx")])
    global chosenFile, summarizer
    print(chosenFile)
    
    # Within file type range
    if file_path:
        # Test
        # print(f"Selected file: {file_path}")

        # Enable summarize button
        # summarizer.config(state='normal', cursor='hand2')

        chosenFile = file_path
        print(f"Selected file: {chosenFile}")
        return chosenFile
    
    else:
        chosenFile = 'Invalid file type'
        print(chosenFile)

# Other Variables
show = True
result = True
chosenFile = 'No chosen file'
filename = ''
fileContent = 'The length of this string is for testing purposes only (placeholder) This is the content of the file This is the content of the file This is the content of the file This is the content of the file This is the content of the file This is the content of the file This is the content of the file This is the content of the file This is the content of the fileThis is the content of the file This is the content of the file This is the content of the file This is the content of the file'
xstAlgoContent = 'The length of this string is for testing purposes only (placeholder) Results based on the existing algorithm  Results based on the existing algorithm Results based on the existing algorithm Results based on the existing algorithm Results based on the existing algorithm Results based on the existing algorithm Results based on the existing algorithm Results based on the existing algorithm Results based on the existing algorithm Results based on the existing algorithm'
newAlgoContent = 'The length of this string is for testing purposes only (placeholder) Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm Results based on the new algorithm'

# Shorten filename displayed if too long
if (len(chosenFile) > 20):
    for i in range(0, 20):
        filename += chosenFile[i]
else:
    filename = chosenFile

# Initialize Screen Size
screenWidth = simu.winfo_screenwidth()
screenHeight = simu.winfo_screenheight()

# Define the Geometry of Simu Window
width = screenWidth * 0.95
height = screenHeight * 0.9
simu.geometry('%dx%d' % (width, height))

# Structure Tip: First lines of codes will be underneath lower lines of codes (in z-index)

# MAIN Background
Frame(simu, background='antiquewhite').pack(fill=BOTH, expand=True)

# ~ ~ ~ ~ ~ ~
# Content
# Content First Column
column1 = Frame(simu, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')

# Display of inserted file
runningFile = Canvas(column1, borderwidth=2, relief='sunken', width=screenWidth * 0.225, height=screenHeight * 0.67)
runningFileFrame = Frame(runningFile)
readFile = Label(runningFileFrame, text=fileContent, wraplength=screenWidth * 0.2, justify='left').pack()

# Display the frame with its content
runningFileFrame.place(anchor=NW, relx=0.05, rely=0.025)
runningFile.pack(side='bottom')

# Insert a File Button
insertFile = Button(column1, text="Insert File", width=15, height=2, borderwidth=2, relief='ridge', cursor='hand2', command=lambda: [summarizer.place_forget(), open_file_dialog(), toggle_Summarizer()])
# insertFile.bind('<Button-1>', )
insertFile.pack(side='left')
textFile = Label(column1, text=filename, padx=5, background='whitesmoke').pack(side='right')

column1.place(relx=0.02, rely=0.14, anchor=NW)
# ~ ~ ~
# Content Second Column
# Column 2
column2 = Frame(simu, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
xstAlgoCanvas = Canvas(column2, borderwidth=2, relief='sunken', width=screenWidth * 0.285, height=screenHeight * 0.67)
xstAlgoFrame = Frame(xstAlgoCanvas)
xstAlgo = Label(xstAlgoFrame, text=xstAlgoContent, wraplength=screenWidth * 0.25, justify='left').pack()

# Display the frame with its content
xstAlgoFrame.place(anchor=NW, relx=0.05, rely=0.025)
xstAlgoCanvas.pack(side='bottom')
# Existing Algorithm Title
Label(column2, text='Existing Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='left')

column2.place(relx=0.4675, rely=0.14, anchor=N)
# ~ ~ ~
# Content Third Column
# Column 3
column3 = Frame(simu, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')

newAlgoCanvas = Canvas(column3, borderwidth=2, relief='sunken', width=screenWidth * 0.285, height=screenHeight * 0.67)
newAlgoFrame = Frame(newAlgoCanvas)
newAlgo = Label(newAlgoFrame, text=newAlgoContent, wraplength=screenWidth * 0.25, justify='left').pack()

# Display the frame with its content
newAlgoFrame.place(anchor=NW, relx=0.05, rely=0.025)
newAlgoCanvas.pack(side='bottom')
# New Algorithm Title
Label(column3, text='NewAlgorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='left')

column3.place(relx=0.98, rely=0.14, anchor=NE)

# Header
# Header Title-- Thesis Title
Label(simu, text="Designing An Adaptive Dynamic Approach Applied in Text Summarization", font=('Slussen Mono Black', 15), background='antiquewhite', width=50, wraplength=screenWidth * 0.45).place(relx=0, rely=0.01, anchor=NW)

# Header Buttons
summarizer = Button(simu, text='Summarize', borderwidth=2, state='disabled', background='antiquewhite', width=12, height=2, activebackground='antiquewhite4', activeforeground="white", disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor')
summarizer.place(relx=0.78, rely=0.05, anchor=NE)

results = Button(simu, text='Results', borderwidth=2, state='disabled', background='antiquewhite', width=12, height=2, activebackground='antiquewhite4', activeforeground="white", disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor')
results.place(relx=0.88, rely=0.05, anchor=NE)

aboutButton = Button(simu, text='About', borderwidth=2, state='normal', background='antiquewhite', width=12, height=2, activebackground='antiquewhite4', activeforeground="white", font=('Calibri Bold', 9), cursor='hand2')
aboutButton.bind('<Button-1>', toggle_About)
aboutButton.place(relx=0.98, rely=0.05, anchor=NE)

# Header About Overlay
aboutWindow = Frame(simu, background='whitesmoke', bd=5, relief='ridge', visual='best', pady=15, padx=15)
Label(aboutWindow, background='whitesmoke', text="Designing An Adaptive Dynamic Approach Applied in Text Summarization", font=('Times New Roman Bold', 13), wraplength=screenWidth * 0.35).pack()
Label(aboutWindow, background='whitesmoke', text="This is the abstract of the study. The abstract of the study contains information that benefits the idea of the research in an instance. Once the readers are enticed by the premise of a study's abstract he/she may begin tackling the matter at hand. This is the abstract of the study. The abstract of the study contains information that benefits the idea of the research in an instance. Once the readers are enticed by the premise of a study's abstract he/she may begin tackling the matter at hand.This is the abstract of the study. The abstract of the study contains information that benefits the idea of the research in an instance. Once the readers are enticed by the premise of a study's abstract he/she may begin tackling the matter at hand.", font=('Times New Roman Normal', 11), wraplength=screenWidth * 0.35, justify='left', pady=30).pack()

# Researchers pack
group_Members = Frame(aboutWindow, background='whitesmoke', height=125, width=screenWidth * 0.35)

# Only PNG are accepted (unless uses Pillow)
tenioPic = PhotoImage(file='./assets/player-spaceship.png').subsample(15, 14)
bajePic = PhotoImage(file='./assets/player-spaceship.png').subsample(15, 14)
caladiaoPic = PhotoImage(file='./assets/player-spaceship.png').subsample(15, 14)

Label(group_Members, text="Tenio", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.95, anchor=NE)
Label(group_Members, image = tenioPic).place(relx=1.05, rely=0.99, anchor=SE)

Label(group_Members, text="Baje", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.7, anchor=N)
Label(group_Members, image = bajePic).place(relx=0.7, rely=0.99, anchor=S)

Label(group_Members, text="Caladiao", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.43, anchor=NW)
Label(group_Members, image = caladiaoPic).place(relx=0.35, rely=0.99, anchor=SW)

# Print Labels
group_Members.pack()

# ~ ~ ~
# Results Window
resultsWindow = Canvas(simu, background='whitesmoke', borderwidth=5, relief='ridge', width=screenWidth * 0.4, height=screenHeight * 0.6)
resultsWindowFrame = Frame(resultsWindow)
Label(resultsWindowFrame, background='whitesmoke', text="Statistics", font=('Times New Roman Bold', 13), wraplength=screenWidth * 0.35).pack()

Label(resultsWindowFrame, background='whitesmoke', text="Relatedness", font=('Times New Roman Normal', 11), wraplength=screenWidth * 0.35, justify='left', pady=30).pack()
# will add Label() text for the grade

Label(resultsWindowFrame, background='whitesmoke', text="Accuracy", font=('Times New Roman Normal', 11), wraplength=screenWidth * 0.35, justify='left', pady=30).pack()
# will add Label() text for the grade

# can add more details/ information for the results of the text summarization

resultsWindowFrame.place(anchor=NW, relx=0.05, rely=0.075)
# Run
simu.mainloop()
