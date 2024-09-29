import tkinter as tk
from tkinter import simpledialog
from file_loader import FileLoader
from text_processor import TextProcessor
from newAlgorithmProcessor import NewAlgorithmProcessor

class UIComponent:
    def __init__(self, parent, TextProcessor, NewAlgorithmProcessor):
        self.parent = parent
        self.text_processor = TextProcessor
        self.new_algorithm_processor = NewAlgorithmProcessor
        self.create_widgets()

    def create_widgets(self):
        self.create_header()
        self.create_columns()
        # Configure main window grid
        self.parent.grid_rowconfigure(0, weight=0)  # Header row
        self.parent.grid_rowconfigure(1, weight=1)  # Columns row
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)
        self.parent.grid_columnconfigure(2, weight=1)

    def create_header(self):
        header_frame = tk.Frame(self.parent, background='#ABDBE6')
        header_frame.grid(row=0, column=0, columnspan=3, sticky='ew')  # Adjusted columnspan to 3

        screen_width = self.parent.winfo_screenwidth()

        tk.Label(header_frame, text="Designing An Adaptive Dynamic Approach Applied in Text Summarization",
                 font=('Slussen Mono Black', 15), background='#ABDBE6', wraplength=screen_width * 0.45).pack(pady=10)

        self.summarizer = tk.Button(header_frame, text='Summarize', borderwidth=2, state='disabled', background='#4D63DA',
                                    width=12, height=2, activebackground='#ABDBE6', activeforeground="white",
                                    disabledforeground='#CACACA', font=('Calibri Bold', 9), cursor='X_cursor', command=self.on_summarize_click)
        self.summarizer.pack(side=tk.RIGHT, padx=5)

        tk.Button(header_frame, text='Results', borderwidth=2, state='disabled', background='#4D63DA',
                  width=12, height=2, activebackground='#ABDBE6', activeforeground="white",
                  disabledforeground='#CACACA', font=('Calibri Bold', 9), cursor='X_cursor').pack(side=tk.RIGHT, padx=5)

        tk.Button(header_frame, text='About', borderwidth=2, state='normal', background='#4D63DA',
                  width=12, height=2, activebackground='#ABDBE6', activeforeground="white",
                  font=('Calibri Bold', 9), cursor='hand2', command=self.open_about_modal).pack(side=tk.RIGHT, padx=5)

        # Add the new button for displaying the memoization table
        self.memo_button = tk.Button(header_frame, text='Show Memo Table', borderwidth=2, state='disabled', background='#4D63DA',
                                     width=15, height=2, activebackground='#ABDBE6', activeforeground="white",
                                     disabledforeground='#CACACA', font=('Calibri Bold', 9), cursor='hand2', command=self.show_memo_table)
        self.memo_button.pack(side=tk.RIGHT, padx=5)

        # Add a new button to clear all data
        self.clear_button = tk.Button(header_frame, text='Clear All', borderwidth=2, state='normal', background='#4D63DA',
                                      width=12, height=2, activebackground='#ABDBE6', activeforeground="white",
                                      font=('Calibri Bold', 9), cursor='hand2', command=self.clear_all_data)
        self.clear_button.pack(side=tk.RIGHT, padx=5)

    def create_columns(self):
        self.create_column1()
        self.create_column2()
        self.create_column3()
        # Configure columns to expand properly
        for i in range(3):
            self.parent.grid_columnconfigure(i, weight=1)
        self.parent.grid_rowconfigure(1, weight=1)

    def create_column1(self):
        self.column1 = tk.Frame(self.parent, padx=15, pady=2, borderwidth=5, relief='groove', background='whitesmoke')
        self.column1.grid(row=1, column=0, sticky='nsew')

        runningFile = tk.Canvas(self.column1, borderwidth=2, relief='sunken')
        runningFileFrame = tk.Frame(runningFile)
        runningFileFrame.pack(fill=tk.BOTH, expand=True)

        self.runningFileLabel = tk.Label(runningFileFrame, wraplength=200, justify='left')
        self.runningFileLabel.pack(fill=tk.BOTH, expand=True)

        runningFile.pack(side='bottom', fill=tk.BOTH, expand=True)

        insertFile = tk.Button(self.column1, text="Insert File", width=15, height=2, borderwidth=5, relief='ridge', cursor='hand2', command=self.on_open_file_click)
        insertFile.pack(side='left', padx=5, pady=5)

        self.fileLabel = tk.Label(self.column1, padx=5, background='whitesmoke')
        self.fileLabel.pack(side='right', padx=5, pady=5)

        # Configure column1 grid
        self.column1.grid_rowconfigure(0, weight=1)
        self.column1.grid_columnconfigure(0, weight=1)

    def create_column2(self):
        column2 = tk.Frame(self.parent, padx=15, pady=2, borderwidth=5, relief='groove', background='whitesmoke')
        column2.grid(row=1, column=1, sticky='nsew')

        xstAlgoCanvas = tk.Canvas(column2, borderwidth=5, relief='sunken')
        xstAlgoFrame = tk.Frame(xstAlgoCanvas)
        xstAlgoFrame.pack(fill=tk.BOTH, expand=True)

        self.xstAlgoLabel = tk.Label(xstAlgoFrame, wraplength=200, justify='left')
        self.xstAlgoLabel.pack(fill=tk.BOTH, expand=True)

        xstAlgoCanvas.pack(side='bottom', fill=tk.BOTH, expand=True)

        tk.Label(column2, text='Existing Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='top')

        self.resultsText = tk.Text(column2, wrap='word', state='disabled')  # Make it read-only
        self.resultsText.pack(expand=True, fill=tk.BOTH)

        # Configure column2 grid
        column2.grid_rowconfigure(0, weight=1)
        column2.grid_columnconfigure(0, weight=1)

    def create_column3(self):
        column3 = tk.Frame(self.parent, padx=15, pady=2, borderwidth=5, relief='groove', background='whitesmoke')
        column3.grid(row=1, column=2, sticky='nsew')

        newAlgoCanvas = tk.Canvas(column3, borderwidth=5, relief='sunken')
        newAlgoFrame = tk.Frame(newAlgoCanvas)
        newAlgoFrame.pack(fill=tk.BOTH, expand=True)

        self.newAlgoLabel = tk.Label(newAlgoFrame, wraplength=200, justify='left')
        self.newAlgoLabel.pack(fill=tk.BOTH, expand=True)

        newAlgoCanvas.pack(side='bottom', fill=tk.BOTH, expand=True)

        tk.Label(column3, text='New Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='top')

        self.newAlgoResultsText = tk.Text(column3, wrap='word', height=10, state='disabled')
        self.newAlgoResultsText.pack(expand=True, fill=tk.BOTH)

        # Configure column3 grid
        column3.grid_rowconfigure(0, weight=1)
        column3.grid_columnconfigure(0, weight=1)

    def on_summarize_click(self):
        # Ensure content is set before summarization
        if not self.text_processor.fileContent:
            print("Error: No content found in text_processor.")
            return

        # Process with the existing algorithm
        summary = self.text_processor.generate_summary()
        self.resultsText.config(state='normal')
        self.resultsText.delete(1.0, tk.END)
        self.resultsText.insert(tk.END, summary)
        self.resultsText.config(state='disabled')

        # Process with the new algorithm
        self.new_algorithm_processor.set_content(self.text_processor.fileContent)
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
        if not filename or not fileContent:
            print("Error: No file selected or file content is empty.")
            return

        self.fileLabel.config(text=filename)
        self.runningFileLabel.config(text=fileContent[:1000] + ('...' if len(fileContent) > 1000 else ''))
        self.text_processor.set_content(fileContent)
        self.summarizer.config(state='normal')
        self.memo_button.config(state='normal')  # Enable memo button when a file is loaded

        # Show Column 1 as a modal
        self.show_column1_modal()

    def show_column1_modal(self):
        # Create a new window to display Column 1 content
        modal = tk.Toplevel(self.parent)
        modal.title("Column 1 Content")
        modal.geometry("400x300")
        modal.transient(self.parent)
        modal.grab_set()

        # Add the content of Column 1 to the modal
        modal_frame = tk.Frame(modal, padx=15, pady=15, background='whitesmoke')
        modal_frame.pack(fill=tk.BOTH, expand=True)

        # Add the runningFileLabel content
        runningFileLabel = tk.Label(modal_frame, text="Running File Content:", font=('Calibri Bold', 12), background='whitesmoke')
        runningFileLabel.pack(anchor='w', pady=20)
        
        runningFileContent = tk.Label(modal_frame, text=self.runningFileLabel.cget("text"), wraplength=350, justify='left', background='whitesmoke')
        runningFileContent.pack(fill=tk.BOTH, expand=True)

        # Add the fileLabel content
        fileLabel = tk.Label(modal_frame, text="File Name:", font=('Calibri Bold', 12), background='whitesmoke')
        fileLabel.pack(anchor='w', pady=5)
        
        fileNameContent = tk.Label(modal_frame, text=self.fileLabel.cget("text"), wraplength=350, justify='left', background='whitesmoke')
        fileNameContent.pack(fill=tk.BOTH, expand=True)

        # Add a Close button to the modal
        tk.Button(modal, text="Close", command=modal.destroy).pack(pady=10)

    def clear_all_data(self):
        # Clear file content and reset UI elements
        self.text_processor.set_content("")
        self.new_algorithm_processor.set_content("")

        self.runningFileLabel.config(text="")
        self.fileLabel.config(text="")
        self.resultsText.config(state='normal')
        self.resultsText.delete(1.0, tk.END)
        self.resultsText.config(state='disabled')

        self.newAlgoResultsText.config(state='normal')
        self.newAlgoResultsText.delete(1.0, tk.END)
        self.newAlgoResultsText.config(state='disabled')

        self.summarizer.config(state='disabled')
        self.memo_button.config(state='disabled')

        # Optionally, clear the memo table
        self.clear_memo_table()

    def clear_memo_table(self):
        # Create a new window to clear the memo table
        memo_window = tk.Toplevel(self.parent)
        memo_window.title("Memoization Table")
        memo_window.geometry("500x400")

        memo_text = tk.Text(memo_window, wrap='word')
        memo_text.pack(expand=True, fill=tk.BOTH)

        memo_text.insert(tk.END, "Memoization table cleared.")
    
    def show_memo_table(self):
        # Create a new window to display the memo table
        memo_window = tk.Toplevel(self.parent)
        memo_window.title("Memoization Table")
        memo_window.geometry("500x400")

        # Create a Text widget to display the memo table contents
        memo_text = tk.Text(memo_window, wrap='word')
        memo_text.pack(expand=True, fill=tk.BOTH)

        # Get the memoization table from text_processor
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

        tk.Label(modal, text="This application is designed to demonstrate text summarization algorithms.",
                 wraplength=350, justify='left').pack(pady=5)

        tk.Button(modal, text="Close", command=modal.destroy).pack(pady=10)
