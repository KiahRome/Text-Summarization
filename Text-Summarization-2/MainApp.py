import tkinter as tk
from file_loader import FileLoader
from text_processor import TextProcessor
from newAlgorithmProcessor import NewAlgorithmProcessor
from userInterface import UIComponent

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Summarization Application")
        self.geometry("1078x768")

        # Initialize processors
        self.text_processor = TextProcessor()
        self.new_algorithm_processor = NewAlgorithmProcessor()

        # Create the UI component
        self.ui = UIComponent(self, self.text_processor, self.new_algorithm_processor)
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
