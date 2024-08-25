from tkinter import *
from tkinter import filedialog

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.show = True
        self.result = True
        self.chosenFile = 'No chosen file'
        self.filename = ''
        self.fileContent = 'The length of this string is for testing purposes only (placeholder) This is the content of the file ...'
        self.xstAlgoContent = 'The length of this string is for testing purposes only (placeholder) Results based on the existing algorithm ...'
        self.newAlgoContent = 'The length of this string is for testing purposes only (placeholder) Results based on the new algorithm ...'
        self.create_widgets()

    def create_widgets(self):
        self.setup_window()
        self.create_header()
        self.create_columns()
        self.create_results_window()

    def setup_window(self):
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.geometry('%dx%d' % (self.screenWidth * 0.95, self.screenHeight * 0.9))
        Frame(self, background='antiquewhite').pack(fill=BOTH, expand=True)

    def create_header(self):
        try:
            self.tenioPic = PhotoImage(file='./player-spaceship.png').subsample(15, 14)
            self.bajePic = PhotoImage(file='./player-spaceship.png').subsample(15, 14)
            self.caladiaoPic = PhotoImage(file='./player-spaceship.png').subsample(15, 14)
        except TclError as e:
            print("Error loading image:", e)
            self.tenioPic = self.bajePic = self.caladiaoPic = None  # Or provide a placeholder image

        Label(self, text="Designing An Adaptive Dynamic Approach Applied in Text Summarization",
              font=('Slussen Mono Black', 15), background='antiquewhite', width=50,
              wraplength=self.screenWidth * 0.45).place(relx=0, rely=0.01, anchor=NW)

        self.summarizer = Button(self, text='Summarize', borderwidth=2, state='disabled', background='antiquewhite',
                                 width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                                 disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor')
        self.summarizer.place(relx=0.78, rely=0.05, anchor=NE)

        self.results = Button(self, text='Results', borderwidth=2, state='disabled', background='antiquewhite',
                              width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                              disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor')
        self.results.place(relx=0.88, rely=0.05, anchor=NE)

        aboutButton = Button(self, text='About', borderwidth=2, state='normal', background='antiquewhite',
                             width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                             font=('Calibri Bold', 9), cursor='hand2', command=self.toggle_about)
        aboutButton.place(relx=0.98, rely=0.05, anchor=NE)

        self.aboutWindow = Frame(self, background='whitesmoke', bd=5, relief='ridge', pady=15, padx=15)
        Label(self.aboutWindow, background='whitesmoke', text="Designing An Adaptive Dynamic Approach Applied in Text Summarization",
              font=('Times New Roman Bold', 13), wraplength=self.screenWidth * 0.35).pack()
        Label(self.aboutWindow, background='whitesmoke', text="This is the abstract of the study...",  # Shortened for brevity
              font=('Times New Roman Normal', 11), wraplength=self.screenWidth * 0.35, justify='left', pady=30).pack()
        self.setup_researchers()

    def setup_researchers(self):
        group_Members = Frame(self.aboutWindow, background='whitesmoke', height=125, width=self.screenWidth * 0.35)
        Label(group_Members, text="Tenio", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.95, anchor=NE)
        Label(group_Members, image=self.tenioPic).place(relx=1.05, rely=0.99, anchor=SE)

        Label(group_Members, text="Baje", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.7, anchor=N)
        Label(group_Members, image=self.bajePic).place(relx=0.7, rely=0.99, anchor=S)

        Label(group_Members, text="Caladiao", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.43, anchor=NW)
        Label(group_Members, image=self.caladiaoPic).place(relx=0.35, rely=0.99, anchor=SW)

        group_Members.pack()

    def create_columns(self):
        self.create_column1()
        self.create_column2()
        self.create_column3()

    def create_column1(self):
        column1 = Frame(self, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        runningFile = Canvas(column1, borderwidth=2, relief='sunken', width=self.screenWidth * 0.225, height=self.screenHeight * 0.67)
        runningFileFrame = Frame(runningFile)
        Label(runningFileFrame, text=self.fileContent, wraplength=self.screenWidth * 0.2, justify='left').pack()
        runningFileFrame.place(anchor=NW, relx=0.05, rely=0.025)
        runningFile.pack(side='bottom')

        insertFile = Button(column1, text="Insert File", width=15, height=2, borderwidth=2, relief='ridge', cursor='hand2', command=self.open_file_dialog)
        insertFile.pack(side='left')
        self.fileLabel = Label(column1, text=self.filename, padx=5, background='whitesmoke')
        self.fileLabel.pack(side='right')

        column1.place(relx=0.02, rely=0.14, anchor=NW)

    def create_column2(self):
        column2 = Frame(self, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        xstAlgoCanvas = Canvas(column2, borderwidth=2, relief='sunken', width=self.screenWidth * 0.285, height=self.screenHeight * 0.67)
        xstAlgoFrame = Frame(xstAlgoCanvas)
        Label(xstAlgoFrame, text=self.xstAlgoContent, wraplength=self.screenWidth * 0.25, justify='left').pack()
        xstAlgoFrame.place(anchor=NW, relx=0.05, rely=0.025)
        xstAlgoCanvas.pack(side='bottom')
        Label(column2, text='Existing Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='left')
        column2.place(relx=0.4675, rely=0.14, anchor=N)

    def create_column3(self):
        column3 = Frame(self, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        newAlgoCanvas = Canvas(column3, borderwidth=2, relief='sunken', width=self.screenWidth * 0.285, height=self.screenHeight * 0.67)
        newAlgoFrame = Frame(newAlgoCanvas)
        Label(newAlgoFrame, text=self.newAlgoContent, wraplength=self.screenWidth * 0.25, justify='left').pack()
        newAlgoFrame.place(anchor=NW, relx=0.05, rely=0.025)
        newAlgoCanvas.pack(side='bottom')
        Label(column3, text='New Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='left')
        column3.place(relx=0.98, rely=0.14, anchor=NE)

    def create_results_window(self):
        self.resultsWindow = Canvas(self, background='whitesmoke', borderwidth=5, relief='ridge', width=self.screenWidth * 0.4, height=self.screenHeight * 0.6)
        resultsWindowFrame = Frame(self.resultsWindow)
        Label(resultsWindowFrame, background='whitesmoke', text="Statistics", font=('Times New Roman Bold', 16)).pack(side='top')
        Label(resultsWindowFrame, background='whitesmoke', text="Some results will be shown here...").pack(side='bottom')
        resultsWindowFrame.pack(fill='both', expand=True)
        self.resultsWindow.place(relx=0.57, rely=0.2, anchor=NW)

    def open_file_dialog(self):
        self.filename = filedialog.askopenfilename()
        self.fileLabel.config(text=self.filename)

    def toggle_about(self):
        if self.show:
            self.aboutWindow.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.show = False
        else:
            self.aboutWindow.place_forget()
            self.show = True

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
