import tkinter as tk
from file_loader import FileLoader
from text_processor import TextProcessor
from userInterface import UIComponent

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Summarizer Application")
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.geometry(f'{int(self.screenWidth * 0.95)}x{int(self.screenHeight * 0.9)}')

        # Initialize components
        self.file_loader = FileLoader()
        self.text_processor = TextProcessor()
        self.ui = UIComponent(self, self.text_processor)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
