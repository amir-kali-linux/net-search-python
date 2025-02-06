#github -----> https://github.com/amir-kali-linux/
import tkinter as tk
import time
from tkinter import Entry, Button
from tkinterweb import HtmlFrame
time.sleep(1)
print("https://github.com/amir-kali-linux/")

class Browser:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Browser")
        self.root.geometry("800x600")

        self.frame = HtmlFrame(root, horizontal_scrollbar="auto")
        self.frame.pack(fill="both", expand=True)

        self.url_entry = Entry(root, font=("Arial", 14))
        self.url_entry.pack(fill="x")

        self.go_button = Button(root, text="Go", command=self.load_url)
        self.go_button.pack()

        self.load_url("http://www.google.com")

    def load_url(self, url=None):
        if url is None:
            url = self.url_entry.get()
        self.frame.load_url(url)

if __name__ == "__main__":
    root = tk.Tk()
    browser = Browser(root)
    root.mainloop()
