import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot with Spectrogram")

        self.label = tk.Label(master, text="Ask your question:")
        self.label.pack()

        self.question = tk.Entry(master)
        self.question.pack()

        self.submit = tk.Button(master, text="Submit", command=self.get_answer)
        self.submit.pack()

        self.answer = tk.Label(master, text="")
        self.answer.pack()

        self.figure = plt.Figure()
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, master)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def get_answer(self):
        # Your chatbot logic here to get the answer for the question
        question = self.question.get()
        answer = "This is a sample answer."

        self.answer.config(text=answer)

        # Create a sample spectrogram
        t = np.arange(0, 3, .01)
        self.ax.cla()
        self.ax.plot(t, 2 * np.sin(2 * np.pi * t))
        self.ax.set_title("Sample Spectrogram")
        self.canvas.draw()

root = tk.Tk()
app = ChatbotGUI(root)
root.mainloop()
