import tkinter as tk
import speech_recognition as sr
import pyttsx3

# Create the main window
root = tk.Tk()
root.title("Voice Assistant Chatbot")
root.geometry("400x300")

# Create the chat window
chatWindow = tk.Text(root, bd=1, bg="white", width=50, height=8)
chatWindow.place(x=6, y=6, height=230, width=370)

# Create the user input field
inputField = tk.Entry(root, font=("Arial", 14))
inputField.place(x=128, y=240, height=40, width=260)

# Create the button to send user input to chatbot
# def send():
#     user_input = inputField.get()
#     chatWindow.insert(tk.END, "You: " + user_input + "\n")
#     inputField.delete(0, tk.END)
#     response = chatbot(user_input)
#     chatWindow.insert(tk.END, "Chatbot: " + response + "\n")
    
# sendButton = tk.Button(root, text="Send", font=("Arial", 14), command=send)
# sendButton.place(x=6, y=240, height=40, width=120)

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Create the button to activate voice input
def activate_voice_input():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio)
            chatWindow.insert(tk.END, "You: " + user_input + "\n")
            response = chatbot(user_input)
            chatWindow.insert(tk.END, "Chatbot: " + response + "\n")
            engine.say(response)
            engine.runAndWait()
        except sr.UnknownValueError:
            chatWindow.insert(tk.END, "Sorry, I did not understand that.\n")
        except sr.RequestError as e:
            chatWindow.insert(tk.END, "Sorry, I could not process your request. {0}\n".format(e))
            
voiceButton = tk.Button(root, text="Activate Voice Input", font=("Arial", 14), command=activate_voice_input)
voiceButton.place(x=210, y=280, height=20, width=180)

# Define the chatbot function to handle user input and generate responses
def chatbot(user_input):
    # Add your chatbot code here to process user input and generate a response
    # For this example, the chatbot just echoes the user input
    return user_input

# Run the main loop
root.mainloop()
