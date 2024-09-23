import tkinter as tk
from file_loader import FileLoader
from text_processor import TextProcessor
from newAlgorithmProcessor import NewAlgorithmProcessor  # Import the new algorithm processor

class UIComponent:
    def __init__(self, parent, text_processor, new_algorithm_processor):
        self.text_processor = text_processor
        self.new_algorithm_processor = new_algorithm_processor  # Initialize new algorithm processor
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.create_header()
        self.create_columns()

    def create_header(self):
        header_frame = tk.Frame(self.parent, background='antiquewhite')
        header_frame.grid(row=0, column=0, columnspan=3, sticky='ew')

        tk.Label(header_frame, text="Designing An Adaptive Dynamic Approach Applied in Text Summarization",
                 font=('Slussen Mono Black', 15), background='antiquewhite', wraplength=self.parent.screenWidth * 0.45).pack(pady=10)

        self.summarizer = tk.Button(header_frame, text='Summarize', borderwidth=2, state='disabled', background='antiquewhite',
                                    width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                                    disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor', command=self.on_summarize_click)
        self.summarizer.pack(side=tk.RIGHT, padx=5)

        tk.Button(header_frame, text='Results', borderwidth=2, state='disabled', background='antiquewhite',
                  width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                  disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor').pack(side=tk.RIGHT, padx=5)

        tk.Button(header_frame, text='About', borderwidth=2, state='normal', background='antiquewhite',
                  width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                  font=('Calibri Bold', 9), cursor='hand2', command=self.open_about_modal).pack(side=tk.RIGHT, padx=5)

        # Add the new button for displaying the memoization table
        self.memo_button = tk.Button(header_frame, text='Show Memo Table', borderwidth=2, state='disabled', background='antiquewhite',
                                    width=15, height=2, activebackground='antiquewhite4', activeforeground="white",
                                    disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='hand2', command=self.show_memo_table)
        self.memo_button.pack(side=tk.RIGHT, padx=5)

    def create_columns(self):
        self.create_column1()
        self.create_column2()
        self.create_column3()

    def create_column1(self):
        column1 = tk.Frame(self.parent, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        column1.grid(row=1, column=0, sticky='nsew')

        runningFile = tk.Canvas(column1, borderwidth=2, relief='sunken')
        runningFileFrame = tk.Frame(runningFile)
        self.runningFileLabel = tk.Label(runningFileFrame, wraplength=self.parent.screenWidth * 0.2, justify='left')
        self.runningFileLabel.pack()
        runningFileFrame.place(anchor=tk.NW, relx=0.05, rely=0.025)
        runningFile.pack(side='bottom', fill=tk.BOTH, expand=True)

        insertFile = tk.Button(column1, text="Insert File", width=15, height=2, borderwidth=2, relief='ridge', cursor='hand2', command=self.on_open_file_click)
        insertFile.pack(side='left', padx=5, pady=5)
        self.fileLabel = tk.Label(column1, padx=5, background='whitesmoke')
        self.fileLabel.pack(side='right', padx=5, pady=5)

    def create_column2(self):
        column2 = tk.Frame(self.parent, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        column2.grid(row=1, column=1, sticky='nsew')

        xstAlgoCanvas = tk.Canvas(column2, borderwidth=2, relief='sunken')
        xstAlgoFrame = tk.Frame(xstAlgoCanvas)
        self.xstAlgoLabel = tk.Label(xstAlgoFrame, wraplength=self.parent.screenWidth * 0.25, justify='left')
        self.xstAlgoLabel.pack()
        xstAlgoFrame.place(anchor=tk.NW, relx=0.05, rely=0.025)
        xstAlgoCanvas.pack(side='bottom', fill=tk.BOTH, expand=True)
        tk.Label(column2, text='Existing Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='top')

        # Create a Text widget in column2 to display results
        self.resultsText = tk.Text(column2, wrap='word', state='disabled')  # Make it read-only
        self.resultsText.pack(expand=True, fill=tk.BOTH)

    def create_column3(self):
        column3 = tk.Frame(self.parent, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        column3.grid(row=1, column=2, sticky='nsew')

        newAlgoCanvas = tk.Canvas(column3, borderwidth=2, relief='sunken')
        newAlgoFrame = tk.Frame(newAlgoCanvas)
        self.newAlgoLabel = tk.Label(newAlgoFrame, wraplength=self.parent.screenWidth * 0.25, justify='left')
        self.newAlgoLabel.pack()
        newAlgoFrame.place(anchor=tk.NW, relx=0.05, rely=0.025)
        newAlgoCanvas.pack(side='bottom', fill=tk.BOTH, expand=True)
        tk.Label(column3, text='New Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='top')

        # Add a Text widget to display the result of the new algorithm
        self.newAlgoResultsText = tk.Text(column3, wrap='word', height=10, state='disabled')
        self.newAlgoResultsText.pack(expand=True, fill=tk.BOTH)

    def on_summarize_click(self):
        # Process with the existing algorithm
        summary = self.text_processor.generate_summary()
        self.resultsText.config(state='normal')
        self.resultsText.delete(1.0, tk.END)
        self.resultsText.insert(tk.END, summary)
        self.resultsText.config(state='disabled')

        # Process with the new algorithm
        self.new_algorithm_processor.set_content(self.text_processor.content)
        new_algo_summary = self.new_algorithm_processor.generate_summary()
        self.newAlgoResultsText.config(state='normal')
        self.newAlgoResultsText.delete(1.0, tk.END)
        self.newAlgoResultsText.insert(tk.END, new_algo_summary)
        self.newAlgoResultsText.config(state='disabled')

        # Show memo table
        self.show_memo_table()

    def on_open_file_click(self):
        file_loader = FileLoader()  # Create an instance of FileLoader
        filename, fileContent = file_loader.open_file()
        if filename:
            self.fileLabel.config(text=filename)
            self.runningFileLabel.config(text=fileContent[:1000] + ('...' if len(fileContent) > 1000 else ''))
            self.text_processor.set_content(fileContent)
            self.summarizer.config(state='normal')
            self.memo_button.config(state='normal')  # Enable memo button when a file is loaded

    def show_memo_table(self):
        # Create a new window to display the memo table
        memo_window = tk.Toplevel(self.parent)
        memo_window.title("Memoization Table")
        memo_window.geometry("500x400")

        # Create a Text widget to display the memo table contents
        memo_text = tk.Text(memo_window, wrap='word')
        memo_text.pack(expand=True, fill=tk.BOTH)

        # Insert memoization table into the Text widget
        memo = self.text_processor.display_memo()
        for sentence, score in memo.items():
            memo_text.insert(tk.END, f"Sentence: {sentence}\nScore: {score}\n\n")

    def open_about_modal(self):
        modal = tk.Toplevel(self.parent)
        modal.title("About")
        modal.geometry("400x300")
        modal.transient(self.parent)
        modal.grab_set()

        tk.Label(modal, text="Designing An Adaptive Dynamic Approach Applied in Text Summarization",
                 font=('Times New Roman Bold', 13), wraplength=350).pack(pady=10)

        tk.Label(modal, text="This is the abstract of the study...", font=('Times New Roman Normal', 11),
                 wraplength=350, justify='left').pack(pady=30)

        self.setup_researchers(modal)

        tk.Button(modal, text="Close", command=modal.destroy).pack(pady=10)

    def setup_researchers(self, parent):
        # Add code to setup researchers' info
        pass
