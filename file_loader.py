from docx import Document

class FileLoader:
    def open_file(self):
        from tkinter import filedialog
        from tkinter import Tk

        root = Tk()
        root.withdraw()  # Hide the root window

        file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if not file_path:
            return None, None

        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return file_path, '\n'.join(full_text)
