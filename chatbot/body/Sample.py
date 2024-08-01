# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
# from PyQt5.QtGui import QFont
# import speech_recognition as sr
# from gtts import gTTS
# from playsound import playsound

# class VoiceAssistantUI(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Initialize the UI elements
#         self.question_label = QLabel(self)
#         self.question_label.setText("Ask me anything:")
#         self.question_label.move(50, 50)
#         self.question_label.setFont(QFont('Arial', 14))

#         self.question_box = QLineEdit(self)
#         self.question_box.move(50, 80)
#         self.question_box.resize(400, 30)

#         self.submit_button = QPushButton('Submit', self)
#         self.submit_button.move(200, 120)
#         self.submit_button.clicked.connect(self.get_answer)

#         self.answer_label = QLabel(self)
#         self.answer_label.move(50, 180)
#         self.answer_label.setFont(QFont('Arial', 14))

#         # Set the window properties
#         self.setGeometry(200, 200, 500, 250)
#         self.setWindowTitle('Voice Assistant')
#         self.show()

#     def get_answer(self):
#         # Use the Google Speech-to-Text API to transcribe the user's question
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             audio = recognizer.listen(source)
#         question = recognizer.recognize_google(audio)

#         # Display the transcribed question in the text box
#         self.question_box.setText(question)

#         # Send the question to your chatbot and get the answer
#         answer = "This is a sample answer."

#         # Use the Google Text-to-Speech API to synthesize the answer
#         tts = gTTS(text=answer, lang='en')
#         tts.save('answer.mp3')

#         # Play the synthesized answer
#         playsound('answer.mp3')

#         # Display the answer in the label
#         self.answer_label.setText(answer)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = VoiceAssistantUI()
#     sys.exit(app.exec_())



#Creating the main window 
# wn = tkinter.Tk() 
# wn.title("DataFlair Voice Assistant")
# wn.geometry('700x300')
# wn.config(bg='LightBlue1')
  
# Label(wn, text='Welcome to meet the Voice Assistant by DataFlair', bg='LightBlue1',
#       fg='black', font=('Courier', 15)).place(x=50, y=10)

# #Button to convert PDF to Audio form
# Button(wn, text="Start", bg='gray',font=('Courier', 15),
#        command=callVoiceAssistant).place(x=290, y=100)

# showCommand=StringVar()
# cmdLabel=Label(wn, textvariable=showCommand, bg='LightBlue1',
#       fg='black', font=('Courier', 15))
# cmdLabel.place(x=250, y=150)

# #Runs the window till it is closed
# wn.mainloop()

# import tkinter as tk
# import tkinter
# import speech_recognition as sr

# def trigger_chatbot(self):
#     # Get user input from the text box
#     user_input = self.input_box.get()

#     # Convert user speech to text
#     with sr.Microphone() as source:
#         self.recognizer.adjust_for_ambient_noise(source)
#         audio = self.recognizer.listen(source)
#     try:
#         user_input = self.recognizer.recognize_google(audio)
#     except sr.UnknownValueError:
#         print("Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print(f"Could not request results from Speech Recognition service: {e}")

#     # Pass user input to chatbot and get response
#     bot_response = self.chatbot_response(user_input)

#     # Add bot response to output text box and speak it
#     self.output_box.insert(tk.END, "You: " + user_input + "\n")
#     self.output_box.insert(tk.END, "Chatbot: " + bot_response + "\n")
#     self.engine.say(bot_response)
#     self.engine.runAndWait()



# #Creating the main window 
# # wn = tkinter.Tk() 
# # from tkinter import Button, Label, StringVar
# # wn.title("DataFlair Voice Assistant")
# # wn.geometry('700x300')
# # wn.config(bg='LightBlue1')
 

# # Label(wn, text='Welcome to meet the Voice Assistant by DataFlair', bg='LightBlue1',
# #       fg='black', font=('Courier', 15)).place(x=50, y=10)

# # def callVoiceAssistant():
# #     print ("calling voice assitant...")
# # #Button to convert PDF to Audio form
# # Button(wn, text="Start", bg='gray',font=('Courier', 15),
# #          command=callVoiceAssistant).place(x=290, y=100)

# # showCommand=StringVar()
# # cmdLabel=Label(wn, textvariable=showCommand, bg='LightBlue1',
# #       fg='black', font=('Courier', 15))
# # cmdLabel.place(x=250, y=150)

# # #Runs the window till it is closed
# # wn.mainloop()




# import tkinter as tk
# import speech_recognition as sr
# import pyttsx3

# # Create the main window
# root = tk.Tk()
# root.title("Voice Assistant Chatbot")
# root.geometry("400x300")

# # Create the chat window
# chatWindow = tk.Text(root, bd=1, bg="white", width=50, height=8)
# chatWindow.place(x=6, y=6, height=230, width=370)

# # Create the user input field
# inputField = tk.Entry(root, font=("Arial", 14))
# inputField.place(x=128, y=240, height=40, width=260)

# # Create the button to send user input to chatbot
# def send():
#     user_input = inputField.get()
#     chatWindow.insert(tk.END, "You: " + user_input + "\n")
#     inputField.delete(0, tk.END)
#     response = chatbot(user_input)
#     chatWindow.insert(tk.END, "Chatbot: " + response + "\n")
    
# sendButton = tk.Button(root, text="Send", font=("Arial", 14), command=send)
# sendButton.place(x=6, y=240, height=40, width=120)

# # Initialize speech recognition and text-to-speech engines
# r = sr.Recognizer()
# engine = pyttsx3.init()

# # Create the button to activate voice input
# def activate_voice_input():
#     with sr.Microphone() as source:
#         print("Speak now...")
#         audio = r.listen(source)
#         try:
#             user_input = r.recognize_google(audio)
#             chatWindow.insert(tk.END, "You: " + user_input + "\n")
#             response = chatbot(user_input)
#             chatWindow.insert(tk.END, "Chatbot: " + response + "\n")
#             engine.say(response)
#             engine.runAndWait()
#         except sr.UnknownValueError:
#             chatWindow.insert(tk.END, "Sorry, I did not understand that.\n")
#         except sr.RequestError as e:
#             chatWindow.insert(tk.END, "Sorry, I could not process your request. {0}\n".format(e))
            
# voiceButton = tk.Button(root, text="Activate Voice Input", font=("Arial", 14), command=activate_voice_input)
# voiceButton.place(x=210, y=280, height=20, width=180)

# # Define the chatbot function to handle user input and generate responses
# def chatbot(user_input):
#     # Add your chatbot code here to process user input and generate a response
#     # For this example, the chatbot just echoes the user input
#     return user_input

# # Run the main loop
# root.mainloop()




import tkinter as tk
import speech_recognition as sr
import pyttsx3

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Voice Assistant Chatbot")
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.create_widgets()

    def create_widgets(self):
        self.message_history = tk.Text(self.window, state=tk.DISABLED)
        self.message_history.pack(fill=tk.BOTH, expand=True)

        self.input_field = tk.Entry(self.window)
        self.input_field.pack(fill=tk.X, pady=10)

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack()

        self.voice_button = tk.Button(self.window, text="Speak", command=self.voice_command)
        self.voice_button.pack()

    def send_message(self):
        message = self.input_field.get()
        # Do something with the message (e.g. pass it to your chatbot)
        self.input_field.delete(0, tk.END)

        self.message_history.configure(state=tk.NORMAL)
        self.message_history.insert(tk.END, f"User: {message}\n")
        # Add chatbot response to message_history
        self.message_history.configure(state=tk.DISABLED)

    def voice_command(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            self.engine.say("Listening...")
            self.engine.runAndWait()
            audio = self.r.listen(source)

        try:
            command = self.r.recognize_google(audio)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, command)
            self.send_message()
        except sr.UnknownValueError:
            self.engine.say("Sorry, I didn't understand that.")
            self.engine.runAndWait()
        except sr.RequestError as e:
            self.engine.say(f"Sorry, there was an error accessing speech recognition: {e}")
            self.engine.runAndWait()

    def run(self):
        self.window.mainloop()

gui = ChatbotGUI()
gui.run()
